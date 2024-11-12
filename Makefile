PROJECT_ROOT                    ?= gnmi/proto
PROTO_PACKAGE                   ?= github.com/openconfig/gnmi/proto
PROTOS                          ?= gnmi_ext/gnmi_ext gnmi/gnmi collector/collector \
                                   target/target
GNMI_TARGET_VERSION             ?= latest

include Makefile.in

### tests/integration/deps
##### ensure integration test dependencies are available
.PHONY: tests/integration/deps
tests/integration/deps:
	$(call command_check,go)
	@{ type gnmi_target > /dev/null 2>&1 \
		|| go install -v github.com/google/gnxi/gnmi_target@$(GNMI_TARGET_VERSION); \
	}

### tests
##### execute tests
.PHONY: tests
tests: | tests/integration/deps
	@poetry run pytest tests/
