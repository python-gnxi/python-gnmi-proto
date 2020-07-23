import json
from typing import Union

import gnmi.proto
import gnmi.proto.legacy


def validate_default_interfaces_get(
    response: Union[gnmi.proto.GetResponse, gnmi.proto.legacy.GetResponse]
):
    assert len(response.notification) == 1

    notification = response.notification.pop()
    assert len(notification.update) == 1

    update = notification.update.pop()
    assert update.val.json_val
    assert json.loads(update.val.json_val.decode("utf-8")) == {
        "interface": {"admin": {"config": {"name": "admin"}, "name": "admin"}}
    }
