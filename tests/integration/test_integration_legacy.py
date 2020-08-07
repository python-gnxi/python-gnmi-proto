import json
import uuid
from typing import List, Tuple

import gnmi.proto.legacy
import grpc
import pytest
from grpc._channel import _InactiveRpcError  # noqa

from tests.integration.validation import (
    validate_default_interfaces_get,
    validate_response_get,
    validate_response_does_not_contain,
)

pytestmark = [pytest.mark.integration]


def test_integration_legacy_permission_denied(service_legacy):
    with pytest.raises(grpc._channel._InactiveRpcError) as e:
        service_legacy.Get(gnmi.proto.legacy.GetRequest())

    assert e.value.code() == grpc.StatusCode.PERMISSION_DENIED


def test_integration_legacy_capabilities(service_legacy):
    response = service_legacy.Capabilities(gnmi.proto.legacy.CapabilityRequest())
    assert isinstance(response, gnmi.proto.legacy.CapabilityResponse)


def test_integration__legacy_get(service_legacy, metadata_legacy):
    response = service_legacy.Get(
        gnmi.proto.legacy.GetRequest(path=[_create_path("interfaces")],),
        metadata=metadata_legacy,
    )

    assert isinstance(response, gnmi.proto.legacy.GetResponse)
    validate_default_interfaces_get(response)


def _update(
    update: gnmi.proto.legacy.Update,
    service_legacy: gnmi.proto.legacy.gNMIStub,
    metadata: List[Tuple[str, str]],
) -> gnmi.proto.legacy.SetResponse:
    response = service_legacy.Set(
        gnmi.proto.legacy.SetRequest(update=[update],), metadata=metadata,
    )
    assert isinstance(response, gnmi.proto.legacy.SetResponse)
    return response


def test_integration_legacy_update_set_string(service_legacy, metadata_legacy):
    new_password = str(uuid.uuid4())
    path = _create_path("system/aaa/authentication/admin-user/config/admin-password")
    update = gnmi.proto.legacy.Update(
        path=path, val=gnmi.proto.legacy.TypedValue(string_val=new_password)
    )
    _update(update, service_legacy, metadata_legacy)

    response = service_legacy.Get(
        gnmi.proto.legacy.GetRequest(path=[path],), metadata=metadata_legacy,
    )
    validate_response_get(response=response, value=new_password)


def test_integration_legacy_update_set_json(service_legacy, metadata_legacy):
    config = {"config": {"timezone-name": "Europe/Berlin"}}
    path = _create_path("system/clock")
    update = gnmi.proto.legacy.Update(
        path=path,
        val=gnmi.proto.legacy.TypedValue(json_ietf_val=json.dumps(config).encode()),
    )
    _update(update, service_legacy, metadata_legacy)

    response = service_legacy.Get(
        gnmi.proto.legacy.GetRequest(path=[path],), metadata=metadata_legacy,
    )
    validate_response_get(response=response, value=config)


def test_integration_legacy_delete(service_legacy, metadata_legacy):
    path = _create_path("system/config/hostname")

    service_legacy.Set(
        gnmi.proto.legacy.SetRequest(delete=[path]), metadata=metadata_legacy
    )

    response = service_legacy.Get(
        gnmi.proto.legacy.GetRequest(path=[_create_path("system/config")],),
        metadata=metadata_legacy,
    )
    validate_response_does_not_contain(response=response, value="hostname")


def _create_path(path) -> gnmi.proto.legacy.Path:
    elements = [gnmi.proto.legacy.PathElem(name=e) for e in path.split("/")]
    return gnmi.proto.legacy.Path(elem=elements)
