PROJECT_ROOT                    ?= gnmi/proto
PROTO_PACKAGE                   ?= github.com/openconfig/gnmi/proto
PROTOS                          ?= gnmi_ext/gnmi_ext gnmi/gnmi collector/collector \
                                   target/target

include Makefile.in
