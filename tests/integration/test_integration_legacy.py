import gnmi.proto.legacy
import grpc
import pytest
from grpc._channel import _InactiveRpcError  # noqa

from tests.integration.validation import validate_default_interfaces_get

pytestmark = [pytest.mark.integration]


def test_integration_legacy_permission_denied(service_legacy):
    with pytest.raises(grpc._channel._InactiveRpcError) as e:
        service_legacy.Get(gnmi.proto.legacy.GetRequest())

    assert e.value.code() == grpc.StatusCode.PERMISSION_DENIED


def test_integration_capabilities(service_legacy):
    response = service_legacy.Capabilities(gnmi.proto.legacy.CapabilityRequest())
    assert isinstance(response, gnmi.proto.legacy.CapabilityResponse)


def test_integration_get(service_legacy, metadata_legacy):
    response = service_legacy.Get(
        gnmi.proto.legacy.GetRequest(
            path=[
                gnmi.proto.legacy.Path(
                    elem=[gnmi.proto.legacy.PathElem(name="interfaces")]
                )
            ],
        ),
        metadata=metadata_legacy,
    )

    assert isinstance(response, gnmi.proto.legacy.GetResponse)
    validate_default_interfaces_get(response)
