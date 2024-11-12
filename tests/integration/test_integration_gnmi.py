import json
import uuid

import gnmi.proto
import grpclib.client
import pytest

from tests.integration.path import create_path
from tests.integration.validation import (
    validate_default_interfaces_get,
    validate_response_get,
)

pytestmark = [pytest.mark.asyncio, pytest.mark.integration]


@pytest.fixture
def get_request_interfaces() -> gnmi.proto.GetRequest:
    return gnmi.proto.GetRequest(
        path=[gnmi.proto.Path(elem=[gnmi.proto.PathElem(name="interfaces")])],
    )


async def test_integration_permission_denied(
    service_unauthenticated, get_request_interfaces
):
    with pytest.raises(grpclib.exceptions.GRPCError) as e:
        await service_unauthenticated.get(get_request_interfaces)

    assert e.value.status == grpclib.Status.PERMISSION_DENIED


async def test_integration_incorrect_credentials(channel, get_request_interfaces):
    service = gnmi.proto.gNMIStub(
        channel, metadata={"username": "username", "password": "password"}
    )
    with pytest.raises(grpclib.exceptions.GRPCError) as e:
        await service.get(get_request_interfaces)

    assert e.value.status == grpclib.Status.PERMISSION_DENIED


async def test_integration_capabilities(service):
    response = await service.capabilities(gnmi.proto.CapabilityRequest([]))
    assert isinstance(response, gnmi.proto.CapabilityResponse)


async def test_integration_get(service, get_request_interfaces):
    response = await service.get(get_request_interfaces)
    assert isinstance(response, gnmi.proto.GetResponse)
    validate_default_interfaces_get(response)


async def test_integration_update_set_string(service):
    new_password = str(uuid.uuid4())
    path = create_path("system/aaa/authentication/admin-user/config/admin-password")
    update = gnmi.proto.Update(
        path=path, val=gnmi.proto.TypedValue(string_val=new_password)
    )
    response = await service.set(
        gnmi.proto.SetRequest(update=[update]),
    )
    assert isinstance(response, gnmi.proto.SetResponse)

    response = await service.get(
        gnmi.proto.GetRequest(path=path),
    )
    validate_response_get(response=response, value=new_password)


async def test_integration_update_set_json(service):
    config = {"config": {"timezone-name": "Europe/Berlin"}}
    path = create_path("system/clock")
    update = gnmi.proto.Update(
        path=path, val=gnmi.proto.TypedValue(json_ietf_val=json.dumps(config).encode())
    )
    response = await service.set(
        gnmi.proto.SetRequest(update=[update]),
    )
    assert isinstance(response, gnmi.proto.SetResponse)

    response = await service.get(
        gnmi.proto.GetRequest(path=path),
    )
    validate_response_get(response=response, value=config)


async def test_integration_delete(service):
    path = create_path("system/clock/config/timezone-name")

    await service.set(gnmi.proto.SetRequest(delete=[path]))

    response = await service.get(
        gnmi.proto.GetRequest(path=create_path("system/clock")),
    )
    validate_response_get(response=response, value={})
