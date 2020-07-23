import gnmi.proto
import grpclib.client
import pytest

# noinspection SpellCheckingInspection
from tests.integration.validation import validate_default_interfaces_get

pytestmark = [pytest.mark.asyncio, pytest.mark.integration]


async def test_integration_permission_denied(service_unauthenticated):
    with pytest.raises(grpclib.exceptions.GRPCError) as e:
        await service_unauthenticated.get()

    assert e.value.status == grpclib.Status.PERMISSION_DENIED


async def test_integration_incorrect_credentials(channel):
    service = gnmi.proto.gNMIStub(
        channel, metadata={"username": "username", "password": "password"}
    )
    with pytest.raises(grpclib.exceptions.GRPCError) as e:
        await service.get()

    assert e.value.status == grpclib.Status.PERMISSION_DENIED


async def test_integration_capabilities(service):
    response = await service.capabilities()
    assert isinstance(response, gnmi.proto.CapabilityResponse)


async def test_integration_get(service):
    response = await service.get(
        path=[gnmi.proto.Path(elem=[gnmi.proto.PathElem(name="interfaces")])],
    )
    assert isinstance(response, gnmi.proto.GetResponse)
    validate_default_interfaces_get(response)
