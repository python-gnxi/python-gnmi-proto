import json
import uuid

import gnmi.proto
import grpclib.client
import pytest

# noinspection SpellCheckingInspection
from tests.integration.validation import (
    validate_default_interfaces_get,
    validate_response_get,
)

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


async def test_integration_update_set_string(service):
    new_password = str(uuid.uuid4())
    path = gnmi.proto.Path(
        elem=[
            gnmi.proto.PathElem(name="system"),
            gnmi.proto.PathElem(name="aaa"),
            gnmi.proto.PathElem(name="authentication"),
            gnmi.proto.PathElem(name="admin-user"),
            gnmi.proto.PathElem(name="config"),
            gnmi.proto.PathElem(name="admin-password"),
        ],
    )
    update = gnmi.proto.Update(
        path=path, val=gnmi.proto.TypedValue(string_val=new_password)
    )
    response = await service.set(update=[update],)
    assert isinstance(response, gnmi.proto.SetResponse)

    response = await service.get(path=path,)
    validate_response_get(response=response, value=new_password)


async def test_integration_update_set_json(service):
    config = {"config": {"timezone-name": "Europe/Berlin"}}
    path = gnmi.proto.Path(
        elem=[gnmi.proto.PathElem(name="system"), gnmi.proto.PathElem(name="clock")],
    )
    update = gnmi.proto.Update(
        path=path, val=gnmi.proto.TypedValue(json_ietf_val=json.dumps(config).encode())
    )
    response = await service.set(update=[update],)
    assert isinstance(response, gnmi.proto.SetResponse)

    response = await service.get(path=path,)
    validate_response_get(response=response, value=config)
