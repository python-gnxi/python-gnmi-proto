# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gnmi/proto/_legacy/gnmi/gnmi.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'gnmi/proto/_legacy/gnmi/gnmi.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from gnmi.proto._legacy.gnmi_ext import gnmi_ext_pb2 as gnmi_dot_proto_dot___legacy_dot_gnmi__ext_dot_gnmi__ext__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"gnmi/proto/_legacy/gnmi/gnmi.proto\x12\x04gnmi\x1a\x19google/protobuf/any.proto\x1a google/protobuf/descriptor.proto\x1a*gnmi/proto/_legacy/gnmi_ext/gnmi_ext.proto\"\x94\x01\n\x0cNotification\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x1a\n\x06prefix\x18\x02 \x01(\x0b\x32\n.gnmi.Path\x12\x1c\n\x06update\x18\x04 \x03(\x0b\x32\x0c.gnmi.Update\x12\x1a\n\x06\x64\x65lete\x18\x05 \x03(\x0b\x32\n.gnmi.Path\x12\x0e\n\x06\x61tomic\x18\x06 \x01(\x08J\x04\x08\x03\x10\x04R\x05\x61lias\"u\n\x06Update\x12\x18\n\x04path\x18\x01 \x01(\x0b\x32\n.gnmi.Path\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0b.gnmi.ValueB\x02\x18\x01\x12\x1d\n\x03val\x18\x03 \x01(\x0b\x32\x10.gnmi.TypedValue\x12\x12\n\nduplicates\x18\x04 \x01(\r\"\x83\x03\n\nTypedValue\x12\x14\n\nstring_val\x18\x01 \x01(\tH\x00\x12\x11\n\x07int_val\x18\x02 \x01(\x03H\x00\x12\x12\n\x08uint_val\x18\x03 \x01(\x04H\x00\x12\x12\n\x08\x62ool_val\x18\x04 \x01(\x08H\x00\x12\x13\n\tbytes_val\x18\x05 \x01(\x0cH\x00\x12\x17\n\tfloat_val\x18\x06 \x01(\x02\x42\x02\x18\x01H\x00\x12\x14\n\ndouble_val\x18\x0e \x01(\x01H\x00\x12*\n\x0b\x64\x65\x63imal_val\x18\x07 \x01(\x0b\x32\x0f.gnmi.Decimal64B\x02\x18\x01H\x00\x12)\n\x0cleaflist_val\x18\x08 \x01(\x0b\x32\x11.gnmi.ScalarArrayH\x00\x12\'\n\x07\x61ny_val\x18\t \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x12\n\x08json_val\x18\n \x01(\x0cH\x00\x12\x17\n\rjson_ietf_val\x18\x0b \x01(\x0cH\x00\x12\x13\n\tascii_val\x18\x0c \x01(\tH\x00\x12\x15\n\x0bproto_bytes\x18\r \x01(\x0cH\x00\x42\x07\n\x05value\"Y\n\x04Path\x12\x13\n\x07\x65lement\x18\x01 \x03(\tB\x02\x18\x01\x12\x0e\n\x06origin\x18\x02 \x01(\t\x12\x1c\n\x04\x65lem\x18\x03 \x03(\x0b\x32\x0e.gnmi.PathElem\x12\x0e\n\x06target\x18\x04 \x01(\t\"j\n\x08PathElem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x03key\x18\x02 \x03(\x0b\x32\x17.gnmi.PathElem.KeyEntry\x1a*\n\x08KeyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"8\n\x05Value\x12\r\n\x05value\x18\x01 \x01(\x0c\x12\x1c\n\x04type\x18\x02 \x01(\x0e\x32\x0e.gnmi.Encoding:\x02\x18\x01\"N\n\x05\x45rror\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x18\x01\"2\n\tDecimal64\x12\x0e\n\x06\x64igits\x18\x01 \x01(\x03\x12\x11\n\tprecision\x18\x02 \x01(\r:\x02\x18\x01\"0\n\x0bScalarArray\x12!\n\x07\x65lement\x18\x01 \x03(\x0b\x32\x10.gnmi.TypedValue\"\x9d\x01\n\x10SubscribeRequest\x12+\n\tsubscribe\x18\x01 \x01(\x0b\x32\x16.gnmi.SubscriptionListH\x00\x12\x1a\n\x04poll\x18\x03 \x01(\x0b\x32\n.gnmi.PollH\x00\x12&\n\textension\x18\x05 \x03(\x0b\x32\x13.gnmi_ext.ExtensionB\t\n\x07requestJ\x04\x08\x04\x10\x05R\x07\x61liases\"\x06\n\x04Poll\"\xa8\x01\n\x11SubscribeResponse\x12$\n\x06update\x18\x01 \x01(\x0b\x32\x12.gnmi.NotificationH\x00\x12\x17\n\rsync_response\x18\x03 \x01(\x08H\x00\x12 \n\x05\x65rror\x18\x04 \x01(\x0b\x32\x0b.gnmi.ErrorB\x02\x18\x01H\x00\x12&\n\textension\x18\x05 \x03(\x0b\x32\x13.gnmi_ext.ExtensionB\n\n\x08response\"\xd5\x02\n\x10SubscriptionList\x12\x1a\n\x06prefix\x18\x01 \x01(\x0b\x32\n.gnmi.Path\x12(\n\x0csubscription\x18\x02 \x03(\x0b\x32\x12.gnmi.Subscription\x12\x1d\n\x03qos\x18\x04 \x01(\x0b\x32\x10.gnmi.QOSMarking\x12)\n\x04mode\x18\x05 \x01(\x0e\x32\x1b.gnmi.SubscriptionList.Mode\x12\x19\n\x11\x61llow_aggregation\x18\x06 \x01(\x08\x12#\n\nuse_models\x18\x07 \x03(\x0b\x32\x0f.gnmi.ModelData\x12 \n\x08\x65ncoding\x18\x08 \x01(\x0e\x32\x0e.gnmi.Encoding\x12\x14\n\x0cupdates_only\x18\t \x01(\x08\"&\n\x04Mode\x12\n\n\x06STREAM\x10\x00\x12\x08\n\x04ONCE\x10\x01\x12\x08\n\x04POLL\x10\x02J\x04\x08\x03\x10\x04R\x0buse_aliases\"\x9f\x01\n\x0cSubscription\x12\x18\n\x04path\x18\x01 \x01(\x0b\x32\n.gnmi.Path\x12$\n\x04mode\x18\x02 \x01(\x0e\x32\x16.gnmi.SubscriptionMode\x12\x17\n\x0fsample_interval\x18\x03 \x01(\x04\x12\x1a\n\x12suppress_redundant\x18\x04 \x01(\x08\x12\x1a\n\x12heartbeat_interval\x18\x05 \x01(\x04\"\x1d\n\nQOSMarking\x12\x0f\n\x07marking\x18\x01 \x01(\r\"\xce\x01\n\nSetRequest\x12\x1a\n\x06prefix\x18\x01 \x01(\x0b\x32\n.gnmi.Path\x12\x1a\n\x06\x64\x65lete\x18\x02 \x03(\x0b\x32\n.gnmi.Path\x12\x1d\n\x07replace\x18\x03 \x03(\x0b\x32\x0c.gnmi.Update\x12\x1c\n\x06update\x18\x04 \x03(\x0b\x32\x0c.gnmi.Update\x12#\n\runion_replace\x18\x06 \x03(\x0b\x32\x0c.gnmi.Update\x12&\n\textension\x18\x05 \x03(\x0b\x32\x13.gnmi_ext.Extension\"\xac\x01\n\x0bSetResponse\x12\x1a\n\x06prefix\x18\x01 \x01(\x0b\x32\n.gnmi.Path\x12$\n\x08response\x18\x02 \x03(\x0b\x32\x12.gnmi.UpdateResult\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0b.gnmi.ErrorB\x02\x18\x01\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12&\n\textension\x18\x05 \x03(\x0b\x32\x13.gnmi_ext.Extension\"\xdd\x01\n\x0cUpdateResult\x12\x15\n\ttimestamp\x18\x01 \x01(\x03\x42\x02\x18\x01\x12\x18\n\x04path\x18\x02 \x01(\x0b\x32\n.gnmi.Path\x12 \n\x07message\x18\x03 \x01(\x0b\x32\x0b.gnmi.ErrorB\x02\x18\x01\x12(\n\x02op\x18\x04 \x01(\x0e\x32\x1c.gnmi.UpdateResult.Operation\"P\n\tOperation\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06\x44\x45LETE\x10\x01\x12\x0b\n\x07REPLACE\x10\x02\x12\n\n\x06UPDATE\x10\x03\x12\x11\n\rUNION_REPLACE\x10\x04\"\x97\x02\n\nGetRequest\x12\x1a\n\x06prefix\x18\x01 \x01(\x0b\x32\n.gnmi.Path\x12\x18\n\x04path\x18\x02 \x03(\x0b\x32\n.gnmi.Path\x12\'\n\x04type\x18\x03 \x01(\x0e\x32\x19.gnmi.GetRequest.DataType\x12 \n\x08\x65ncoding\x18\x05 \x01(\x0e\x32\x0e.gnmi.Encoding\x12#\n\nuse_models\x18\x06 \x03(\x0b\x32\x0f.gnmi.ModelData\x12&\n\textension\x18\x07 \x03(\x0b\x32\x13.gnmi_ext.Extension\";\n\x08\x44\x61taType\x12\x07\n\x03\x41LL\x10\x00\x12\n\n\x06\x43ONFIG\x10\x01\x12\t\n\x05STATE\x10\x02\x12\x0f\n\x0bOPERATIONAL\x10\x03\"\x7f\n\x0bGetResponse\x12(\n\x0cnotification\x18\x01 \x03(\x0b\x32\x12.gnmi.Notification\x12\x1e\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x0b.gnmi.ErrorB\x02\x18\x01\x12&\n\textension\x18\x03 \x03(\x0b\x32\x13.gnmi_ext.Extension\";\n\x11\x43\x61pabilityRequest\x12&\n\textension\x18\x01 \x03(\x0b\x32\x13.gnmi_ext.Extension\"\xaa\x01\n\x12\x43\x61pabilityResponse\x12)\n\x10supported_models\x18\x01 \x03(\x0b\x32\x0f.gnmi.ModelData\x12+\n\x13supported_encodings\x18\x02 \x03(\x0e\x32\x0e.gnmi.Encoding\x12\x14\n\x0cgNMI_version\x18\x03 \x01(\t\x12&\n\textension\x18\x04 \x03(\x0b\x32\x13.gnmi_ext.Extension\"@\n\tModelData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0corganization\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t*D\n\x08\x45ncoding\x12\x08\n\x04JSON\x10\x00\x12\t\n\x05\x42YTES\x10\x01\x12\t\n\x05PROTO\x10\x02\x12\t\n\x05\x41SCII\x10\x03\x12\r\n\tJSON_IETF\x10\x04*A\n\x10SubscriptionMode\x12\x12\n\x0eTARGET_DEFINED\x10\x00\x12\r\n\tON_CHANGE\x10\x01\x12\n\n\x06SAMPLE\x10\x02\x32\xe3\x01\n\x04gNMI\x12\x41\n\x0c\x43\x61pabilities\x12\x17.gnmi.CapabilityRequest\x1a\x18.gnmi.CapabilityResponse\x12*\n\x03Get\x12\x10.gnmi.GetRequest\x1a\x11.gnmi.GetResponse\x12*\n\x03Set\x12\x10.gnmi.SetRequest\x1a\x11.gnmi.SetResponse\x12@\n\tSubscribe\x12\x16.gnmi.SubscribeRequest\x1a\x17.gnmi.SubscribeResponse(\x01\x30\x01:3\n\x0cgnmi_service\x12\x1c.google.protobuf.FileOptions\x18\xe9\x07 \x01(\tBF\n\x15\x63om.github.gnmi.protoB\tGnmiProtoP\x01Z\x17gnmi/proto/_legacy/gnmi\xca>\x06\x30.10.0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gnmi.proto._legacy.gnmi.gnmi_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.github.gnmi.protoB\tGnmiProtoP\001Z\027gnmi/proto/_legacy/gnmi\312>\0060.10.0'
  _globals['_UPDATE'].fields_by_name['value']._loaded_options = None
  _globals['_UPDATE'].fields_by_name['value']._serialized_options = b'\030\001'
  _globals['_TYPEDVALUE'].fields_by_name['float_val']._loaded_options = None
  _globals['_TYPEDVALUE'].fields_by_name['float_val']._serialized_options = b'\030\001'
  _globals['_TYPEDVALUE'].fields_by_name['decimal_val']._loaded_options = None
  _globals['_TYPEDVALUE'].fields_by_name['decimal_val']._serialized_options = b'\030\001'
  _globals['_PATH'].fields_by_name['element']._loaded_options = None
  _globals['_PATH'].fields_by_name['element']._serialized_options = b'\030\001'
  _globals['_PATHELEM_KEYENTRY']._loaded_options = None
  _globals['_PATHELEM_KEYENTRY']._serialized_options = b'8\001'
  _globals['_VALUE']._loaded_options = None
  _globals['_VALUE']._serialized_options = b'\030\001'
  _globals['_ERROR']._loaded_options = None
  _globals['_ERROR']._serialized_options = b'\030\001'
  _globals['_DECIMAL64']._loaded_options = None
  _globals['_DECIMAL64']._serialized_options = b'\030\001'
  _globals['_SUBSCRIBERESPONSE'].fields_by_name['error']._loaded_options = None
  _globals['_SUBSCRIBERESPONSE'].fields_by_name['error']._serialized_options = b'\030\001'
  _globals['_SETRESPONSE'].fields_by_name['message']._loaded_options = None
  _globals['_SETRESPONSE'].fields_by_name['message']._serialized_options = b'\030\001'
  _globals['_UPDATERESULT'].fields_by_name['timestamp']._loaded_options = None
  _globals['_UPDATERESULT'].fields_by_name['timestamp']._serialized_options = b'\030\001'
  _globals['_UPDATERESULT'].fields_by_name['message']._loaded_options = None
  _globals['_UPDATERESULT'].fields_by_name['message']._serialized_options = b'\030\001'
  _globals['_GETRESPONSE'].fields_by_name['error']._loaded_options = None
  _globals['_GETRESPONSE'].fields_by_name['error']._serialized_options = b'\030\001'
  _globals['_ENCODING']._serialized_start=3443
  _globals['_ENCODING']._serialized_end=3511
  _globals['_SUBSCRIPTIONMODE']._serialized_start=3513
  _globals['_SUBSCRIPTIONMODE']._serialized_end=3578
  _globals['_NOTIFICATION']._serialized_start=150
  _globals['_NOTIFICATION']._serialized_end=298
  _globals['_UPDATE']._serialized_start=300
  _globals['_UPDATE']._serialized_end=417
  _globals['_TYPEDVALUE']._serialized_start=420
  _globals['_TYPEDVALUE']._serialized_end=807
  _globals['_PATH']._serialized_start=809
  _globals['_PATH']._serialized_end=898
  _globals['_PATHELEM']._serialized_start=900
  _globals['_PATHELEM']._serialized_end=1006
  _globals['_PATHELEM_KEYENTRY']._serialized_start=964
  _globals['_PATHELEM_KEYENTRY']._serialized_end=1006
  _globals['_VALUE']._serialized_start=1008
  _globals['_VALUE']._serialized_end=1064
  _globals['_ERROR']._serialized_start=1066
  _globals['_ERROR']._serialized_end=1144
  _globals['_DECIMAL64']._serialized_start=1146
  _globals['_DECIMAL64']._serialized_end=1196
  _globals['_SCALARARRAY']._serialized_start=1198
  _globals['_SCALARARRAY']._serialized_end=1246
  _globals['_SUBSCRIBEREQUEST']._serialized_start=1249
  _globals['_SUBSCRIBEREQUEST']._serialized_end=1406
  _globals['_POLL']._serialized_start=1408
  _globals['_POLL']._serialized_end=1414
  _globals['_SUBSCRIBERESPONSE']._serialized_start=1417
  _globals['_SUBSCRIBERESPONSE']._serialized_end=1585
  _globals['_SUBSCRIPTIONLIST']._serialized_start=1588
  _globals['_SUBSCRIPTIONLIST']._serialized_end=1929
  _globals['_SUBSCRIPTIONLIST_MODE']._serialized_start=1872
  _globals['_SUBSCRIPTIONLIST_MODE']._serialized_end=1910
  _globals['_SUBSCRIPTION']._serialized_start=1932
  _globals['_SUBSCRIPTION']._serialized_end=2091
  _globals['_QOSMARKING']._serialized_start=2093
  _globals['_QOSMARKING']._serialized_end=2122
  _globals['_SETREQUEST']._serialized_start=2125
  _globals['_SETREQUEST']._serialized_end=2331
  _globals['_SETRESPONSE']._serialized_start=2334
  _globals['_SETRESPONSE']._serialized_end=2506
  _globals['_UPDATERESULT']._serialized_start=2509
  _globals['_UPDATERESULT']._serialized_end=2730
  _globals['_UPDATERESULT_OPERATION']._serialized_start=2650
  _globals['_UPDATERESULT_OPERATION']._serialized_end=2730
  _globals['_GETREQUEST']._serialized_start=2733
  _globals['_GETREQUEST']._serialized_end=3012
  _globals['_GETREQUEST_DATATYPE']._serialized_start=2953
  _globals['_GETREQUEST_DATATYPE']._serialized_end=3012
  _globals['_GETRESPONSE']._serialized_start=3014
  _globals['_GETRESPONSE']._serialized_end=3141
  _globals['_CAPABILITYREQUEST']._serialized_start=3143
  _globals['_CAPABILITYREQUEST']._serialized_end=3202
  _globals['_CAPABILITYRESPONSE']._serialized_start=3205
  _globals['_CAPABILITYRESPONSE']._serialized_end=3375
  _globals['_MODELDATA']._serialized_start=3377
  _globals['_MODELDATA']._serialized_end=3441
  _globals['_GNMI']._serialized_start=3581
  _globals['_GNMI']._serialized_end=3808
# @@protoc_insertion_point(module_scope)
