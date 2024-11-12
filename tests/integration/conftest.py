from typing import List, Tuple

import gnmi.proto
import gnmi.proto.legacy
import grpc
import grpclib.client
import pytest
import pytest_asyncio

from tests.integration.target import Target, TargetConfig


@pytest.fixture
def target_config() -> TargetConfig:
    return TargetConfig()


@pytest_asyncio.fixture
async def target(target_config) -> Target:
    async with Target(config=target_config) as t:
        yield t


@pytest.fixture
def channel(target) -> grpclib.client.Channel:
    return grpclib.client.Channel(host="127.0.0.1", port=target.config.port, ssl=None)


@pytest.fixture
def channel_legacy(target) -> grpc.Channel:
    return grpc.insecure_channel(f"127.0.0.1:{target.config.port}")


@pytest.fixture
def service(target, channel) -> gnmi.proto.gNMIStub:
    return gnmi.proto.gNMIStub(
        channel,
        metadata={
            "username": target.config.username,
            "password": target.config.password,
        },
    )


@pytest.fixture
def service_unauthenticated(channel) -> gnmi.proto.gNMIStub:
    return gnmi.proto.gNMIStub(channel)


@pytest.fixture
def service_legacy(target, channel_legacy) -> gnmi.proto.legacy.gNMIStub:
    return gnmi.proto.legacy.gNMIStub(
        channel_legacy,
    )


@pytest.fixture
def metadata_legacy(target) -> List[Tuple[str, str]]:
    return [("username", target.config.username), ("password", target.config.password)]
