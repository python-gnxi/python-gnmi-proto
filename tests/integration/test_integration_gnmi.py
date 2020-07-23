import json

import gnmi.proto
import grpclib.client
import pytest

# noinspection SpellCheckingInspection
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
    assert len(response.notification) == 1

    notification = response.notification.pop()
    assert len(notification.update) == 1

    update = notification.update.pop()
    assert update.val.json_val
    assert json.loads(update.val.json_val.decode("utf-8")) == {
        "interface": {"admin": {"config": {"name": "admin"}, "name": "admin"}}
    }
