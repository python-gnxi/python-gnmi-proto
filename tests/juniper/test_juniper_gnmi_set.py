import grpclib.client
import pytest
import gnmi.proto
import json

pytestmark = [pytest.mark.asyncio]


async def test_juniper_set_leaf_value():
    channel = grpclib.client.Channel(host="<insert-switch-ip>", port=57400, ssl=None)
    stub = gnmi.proto.gNMIStub(
        channel,
        metadata={"username": "<insert-username>", "password": "<insert-password>"},
    )

    path = gnmi.proto.Path(
        element=[],
        origin="juniper",
        elem=[
            gnmi.proto.PathElem(name="configuration", key={}),
            gnmi.proto.PathElem(name="interfaces", key={}),
            gnmi.proto.PathElem(name="interface", key={"name": "ge-0/0/0"}),
            gnmi.proto.PathElem(name="description", key={}),
        ],
        target="",
    )

    value = gnmi.proto.TypedValue(json_val=json.dumps("new description").encode())

    await stub.set(update=[gnmi.proto.Update(path=path, val=value)])


# This does not work. Error is: grpclib.exceptions.GRPCError: (<Status.INVALID_ARGUMENT: 3>, 'syntax error, expecting "@";', None)
async def test_juniper_set_value_on_container():
    channel = grpclib.client.Channel(host="<insert-switch-ip>", port=57400, ssl=None)
    stub = gnmi.proto.gNMIStub(
        channel,
        metadata={"username": "<insert-username>", "password": "<insert-password>"},
    )

    path = gnmi.proto.Path(
        element=[],
        origin="juniper",
        elem=[
            gnmi.proto.PathElem(name="configuration", key={}),
            gnmi.proto.PathElem(name="interfaces", key={}),
            gnmi.proto.PathElem(name="interface", key={"name": "ge-0/0/0"}),
        ],
        target="",
    )

    value = gnmi.proto.TypedValue(
        json_val=json.dumps({"description": "new description"}).encode()
    )

    await stub.set(update=[gnmi.proto.Update(path=path, val=value)])
