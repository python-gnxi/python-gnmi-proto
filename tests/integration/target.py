import asyncio
import sys
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from random import randint
from typing import List, Optional

from tests.integration import INTEGRATION_FIXTURES_DIR


@dataclass
class TargetConfig:
    file: Path = field(default=INTEGRATION_FIXTURES_DIR.joinpath("config.json"))
    port: int = field(default_factory=lambda: randint(9000, 9500))
    username: str = field(default_factory=lambda: str(uuid.uuid4()))
    password: str = field(default_factory=lambda: str(uuid.uuid4()))
    options: List[str] = field(default_factory=list)

    @property
    def command_args(self) -> List[str]:
        args = [
            "-bind_address",
            f":{self.port}",
            "-notls",
            "-logtostderr",
            "-username",
            self.username,
            "-password",
            self.password,
            *self.options,
        ]

        if self.file:
            args.append("-config")
            args.append(self.file.as_posix())

        return args


class Target:
    _CMD = "gnmi_target"

    def __init__(self, config: Optional[TargetConfig] = None):
        self.config = config or TargetConfig()
        self._process = None

    @property
    def process(self) -> asyncio.subprocess.Process:
        return self._process

    async def __aenter__(self):
        self._process = await asyncio.create_subprocess_exec(
            self._CMD,
            *self.config.command_args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._process.kill()

        # push output to allow for capture
        stdout, stderr = await self.process.communicate()
        sys.stdout.write(stdout.decode())
        sys.stderr.write(stderr.decode())
