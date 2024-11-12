# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: github.com/openconfig/gnmi/proto/target/target.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    Dict,
    List,
)

import betterproto

from .. import gnmi as _gnmi__


@dataclass(eq=False, repr=False)
class Configuration(betterproto.Message):
    """
    Configuration holds all information necessary for a caching gNMI collector
     to establish subscriptions to a list of gNMI targets.
    """

    request: Dict[str, "_gnmi__.SubscribeRequest"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    """
    Request is a keyed list of all SubscriptionRequests that can be sent
     to targets in the Configuration.
     The request must have at minimum a SubscriptionList with a prefix
     containing origin and one or more Subscriptions.  Only the STREAM mode is
     supported.
    """

    target: Dict[str, "Target"] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    """
    Target is the full list of targets connected to by a caching gNMI
     collector.  The key of the map is a unique name to identify a target and
     is set in the prefix.target of a SubscriptionRequest message when
     connecting to each respective target.
    """

    instance_id: str = betterproto.string_field(3)
    """Identifier for the caching collector."""

    meta: Dict[str, str] = betterproto.map_field(
        4, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    """Additional config metadata."""

    revision: int = betterproto.int64_field(536870911)
    """
    Revision for this Configuration. Systems that non-atomically write
     configuration should populate and require revision, leveraging canonical
     protobuf serialization of fields in order. Presence of this field makes no
     guarantee. Consumers should account for atomicity constraints of their
     environment and any custom encoding.
    """


@dataclass(eq=False, repr=False)
class Target(betterproto.Message):
    """
    Target is the information necessary to establish a single gNMI Subscribe RPC
     to be collected and cached.
    """

    addresses: List[str] = betterproto.string_field(1)
    """
    A list of address and port or name that resolves to an address and port.
    """

    credentials: "Credentials" = betterproto.message_field(2)
    """Credentials to use in metadata for authorization of the RPC"""

    request: str = betterproto.string_field(3)
    """
    The request to be sent to the target. The string supplied is looked up in
     the request map of the Configuration message.
    """

    meta: Dict[str, str] = betterproto.map_field(
        4, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    """Additional target metadata."""

    dialer: str = betterproto.string_field(5)
    """
    How should the target be dialed. This option allows for a custom
     implementation for how this target is to be reached. If unset the
     collector's default implementation will be used.
    """


@dataclass(eq=False, repr=False)
class Credentials(betterproto.Message):
    """
    Credentials contains the fields necessary for authentication of the client to
     the target.
    """

    username: str = betterproto.string_field(1)
    password: str = betterproto.string_field(2)
    password_id: str = betterproto.string_field(3)
    """Password lookup ID."""
