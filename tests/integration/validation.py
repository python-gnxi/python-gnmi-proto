import json
from typing import Any, Dict, Union

import gnmi.proto
import gnmi.proto.legacy


def validate_response_get(
    response: Union[gnmi.proto.GetResponse, gnmi.proto.legacy.GetResponse],
    value: Union[str, Dict[str, Any]],
):
    assert len(response.notification) == 1

    notification = response.notification.pop()
    assert len(notification.update) == 1

    update = notification.update.pop()

    if isinstance(value, str):
        assert update.val.string_val == value
    else:
        assert update.val.json_val
        assert json.loads(update.val.json_val.decode("utf-8")) == value


def validate_default_interfaces_get(
    response: Union[gnmi.proto.GetResponse, gnmi.proto.legacy.GetResponse],
):
    validate_response_get(
        response=response,
        value={"interface": {"admin": {"config": {"name": "admin"}, "name": "admin"}}},
    )


def validate_response_does_not_contain(
    response: Union[gnmi.proto.GetResponse, gnmi.proto.legacy.GetResponse], value: str
):
    assert len(response.notification) == 1

    notification = response.notification.pop()
    assert len(notification.update) == 1

    update = notification.update.pop()
    assert value not in update.val.json_val.decode("utf-8")
