from gnmi.proto._legacy.collector.collector_pb2_grpc import (  # noqa
    Collector,
    CollectorServicer,
    CollectorStub,
)

from gnmi.proto._legacy.collector.collector_pb2 import (  # noqa
    Nil,
    ReconnectRequest,
)

from gnmi.proto._legacy.target.target_pb2 import (  # noqa
    Configuration,
    Credentials,
    Target,
)

from gnmi.proto._legacy.gnmi_ext.gnmi_ext_pb2 import (  # noqa
    Extension,
    ExtensionID,
    MasterArbitration,
    RegisteredExtension,
    Role,
)

from gnmi.proto._legacy.gnmi.gnmi_pb2_grpc import (  # noqa
    gNMI,
    gNMIServicer,
    gNMIStub,
)

from gnmi.proto._legacy.gnmi.gnmi_pb2 import (  # noqa
    Alias,
    AliasList,
    ASCII,
    BYTES,
    CapabilityRequest,
    CapabilityResponse,
    Encoding,
    Error,
    GetRequest,
    GetResponse,
    JSON,
    ModelData,
    Notification,
    Path,
    PathElem,
    Poll,
    PROTO,
    QOSMarking,
    SAMPLE,
    ScalarArray,
    SetRequest,
    SetResponse,
    SubscribeRequest,
    SubscribeResponse,
    Subscription,
    SubscriptionList,
    SubscriptionMode,
    TypedValue,
    Update,
    UpdateResult,
    Value,
)
