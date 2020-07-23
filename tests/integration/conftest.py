import gnmi.proto
import grpclib.client
import pytest

from tests.integration.target import Target, TargetConfig


@pytest.fixture
def target_config() -> TargetConfig:
    return TargetConfig()


@pytest.fixture
async def target(target_config) -> Target:
    async with Target(config=target_config) as t:
        yield t


@pytest.fixture
def channel(target) -> grpclib.client.Channel:
    return grpclib.client.Channel(host="127.0.0.1", port=target.config.port, ssl=None)


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
