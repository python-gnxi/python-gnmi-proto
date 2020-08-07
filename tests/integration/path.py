import gnmi.proto
import gnmi.proto.legacy


def create_legacy_path(path) -> gnmi.proto.legacy.Path:
    elements = [gnmi.proto.legacy.PathElem(name=e) for e in path.split("/")]
    return gnmi.proto.legacy.Path(elem=elements)


def create_path(path) -> gnmi.proto.Path:
    elements = [gnmi.proto.PathElem(name=e) for e in path.split("/")]
    return gnmi.proto.Path(elem=elements)
