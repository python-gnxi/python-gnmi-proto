# gNMI Protobuf
[![PyPI version](https://badge.fury.io/py/gnmi-proto.svg)](https://badge.fury.io/py/gnmi-proto)
[![Python Versions](https://img.shields.io/pypi/pyversions/gnmi-proto)](https://pypi.org/project/gnmi-proto/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![](https://github.com/python-gnxi/python-gnmi-proto/workflows/Test%20Suite/badge.svg)](https://github.com/python-gnxi/python-gnmi-proto/actions?query=workflow%3A%22Test+Suite%22)


This project aims to be a base building block for [gNMI](https://github.com/openconfig/gnmi) projects written in Python.

The process of building pythonic libraries and applications using [gRPC](https://grpc.io/) and [Protocol Buffers] have been fragmented. This often means that a developer needs to copy over `proto` files, generate Python source from these using `protoc` and use them in-tree for their project. There already exists several projects built in this fashion. While functional, these can be hard to reuse or maintain, often times resulting stale code and no versioning.

`gnmi-proto` builds on top of the improvement already done by [betterproto](https://pypi.org/project/betterproto/) and in turn by the [grpclib](https://pypi.org/project/grpclib/) library. Here, we make available, as versioned packages, code generated from [gNMI protocol buffers](https://github.com/openconfig/gnmi/tree/master/proto).

The default implementation makes use of the [betterproto](https://pypi.org/project/betterproto/) `protoc` plugin to generate clean modern code. In addition, this also provides a `gnmi.proto.legacy` module exposing code generated by `protoc` using the the in-built Python generator.

## Example Usage
### Client
The following code expects a server at `127.0.0.1:9339` with the [test configuration](https://github.com/python-gnxi/python-gnmi-proto/blob/master/tests/integration/fixtures/config.json). Refer to [gNMI Target Server](https://github.com/python-gnxi/python-gnmi-proto/blob/master/CONTRIBUTING.md#gnmi-target-server) section in [CONTRIBUTING.md](https://github.com/python-gnxi/python-gnmi-proto/blob/master/CONTRIBUTING.md) for information on how to set it up.

#### Using betterproto and grpclib
```py  
import gnmi.proto
import grpclib.client


async def main():
    channel = grpclib.client.Channel(host="127.0.0.1", port=9339, ssl=None)
    service = gnmi.proto.gNMIStub(
        channel, metadata={"username": "admin", "password": "secret",},
    )
    
    response = await service.capabilities()
    print(response.to_json(indent=2))

    response = await service.get(
        path=[gnmi.proto.Path(elem=[gnmi.proto.PathElem(name="interfaces")])],
    )
    print(response.to_json(indent=2))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

```

#### Using vanilla grpc
```py
import gnmi.proto.legacy
import grpc


def main():
    channel = grpc.insecure_channel("127.0.0.1:9339")
    metadata = [("username", "admin"), ("password", "secret")]
    service = gnmi.proto.legacy.gNMIStub(channel)

    response = service.Capabilities(gnmi.proto.legacy.CapabilityRequest())
    print(response)

    response = service.Get(
        gnmi.proto.legacy.GetRequest(
            path=[
                gnmi.proto.legacy.Path(
                    elem=[gnmi.proto.legacy.PathElem(name="interfaces")]
                )
            ],
        ),
        metadata=metadata,
    )
    print(response)


if __name__ == "__main__":
    main()

```
