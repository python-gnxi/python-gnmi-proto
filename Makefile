MAKEFILE_PATH                   := $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT_DIR                        := $(patsubst %/,%,$(dir $(MAKEFILE_PATH)))

SRC_DIR                         := $(ROOT_DIR)/src
TESTS_DIR                       := $(ROOT_DIR)/tests
VENDOR_DIR                      := $(ROOT_DIR)/vendor

PROTO_PACKAGE                   ?= github.com/openconfig/gnmi/proto
PROTO_PATH                      := $(VENDOR_DIR)/$(PROTO_PACKAGE)

PACKAGE_BETTERPROTO             ?= gnmi/proto/_internal
PACKAGE_BETTERPROTO_PATH        := $(SRC_DIR)/$(PACKAGE_BETTERPROTO)

PACKAGE_LEGACY                  ?= gnmi/proto/_legacy
PACKAGE_LEGACY_PATH             := $(SRC_DIR)/$(PACKAGE_LEGACY)

define USAGE

This makefile provides a sugar-coated interface for automation of
development environment tasks/chores and also provides a easy-to-use
interface for ci-jobs.

	Usage: make <target>

If you would like see target specific help (where available) use
	$ make <target>/help

endef
export USAGE

.PHONY:all
all:
	@echo "$$USAGE"

define command_check
	@type $(1) > /dev/null 2>&1 || {\
		echo 1>&2 "$(1) command not found in \$$PATH"; exit 1;\
	}
endef

# custom wrapper to generate python source from gnmi proto files using default python
define protoc-legacy
	@echo "Regenerating legacy python code for $(1) ..."
	@{\
		install -d $(PACKAGE_LEGACY_PATH);\
		proto=$(1);\
		src="$(PROTO_PATH)/$${proto}/$${proto}.proto";\
		dst="$(PACKAGE_LEGACY_PATH)/$${proto}/$${proto}.proto";\
		install -D $${src} $${dst};\
		touch $$(dirname $${dst}/__init__.py);\
		sed -i s+'^option go_package = "$(PROTO_PACKAGE)'+'option go_package = "$(PACKAGE_LEGACY)'+g $${dst};\
		sed -i s+'^import "$(PROTO_PACKAGE)'+'import "$(PACKAGE_LEGACY)'+g $${dst};\
		poetry run python -m grpc.tools.protoc \
			--proto_path="$(SRC_DIR)/" \
			--python_out=$(SRC_DIR)/ \
			--grpc_python_out=$(SRC_DIR)/ $${dst};\
	}
endef

.PHONY: %/help
%/help: HELP_TARGET = $(subst /help,,$@)
%/help:
	@make -C $(ROOT_DIR) help | grep -Pzo "\n$(HELP_TARGET)(/\w+)*:.*(\n\s+(.*)?)*\n" \
		|| echo >&2 "No help found. You are on your own. All alone. In this big bad world."

### help:
##### displays this help message.
.PHONY: help
help: | all
	@grep -P '^\s*###* ' $(MAKEFILE_LIST) | sed s/'\s*### '// | sed s/'#'/'    '/g

### debug/show/vars:
##### debug target to list all variables and their values.
.PHONY: debug/show/vars
debug/show/vars:
	@echo "===================================================================="
	@echo "MAKEFILE_PATH                   = $(MAKEFILE_PATH)"
	@echo "ROOT_DIR                        = $(ROOT_DIR)"
	@echo "TESTS_DIR                       = $(TESTS_DIR)"
	@echo "SHELL                           = $(SHELL)"
	@echo "===================================================================="

### check/commands:
##### Checks if all required commands are available.
.PHONY: check/commands
check/commands:
	$(call command_check,poetry)
	$(call command_check,git)

### update/vendor
##### updated vendored source
.PHONY: update/vendor
update/vendor: | check/commands
	@echo "Updating git submodules ..."
	@git submodule update --init --recursive

### update/proto/legacy
##### regenerate legacy source from proto files
.PHONY: update/proto/legacy
update/proto/legacy:
	$(call protoc-legacy,gnmi_ext)
	$(call protoc-legacy,gnmi)
	$(call protoc-legacy,collector)
	$(call protoc-legacy,target)

### update/proto
##### regenerate source from proto files
.PHONY: update/proto
update/proto:
	@echo "Regenerating betterproto source ..."
	@poetry run python -m grpc.tools.protoc --proto_path="$(VENDOR_DIR):$(ROOT_DIR)" \
		--python_betterproto_out=$(PACKAGE_BETTERPROTO_PATH) \
		$(PROTO_PATH)/gnmi/gnmi.proto \
		$(PROTO_PATH)/gnmi_ext/gnmi_ext.proto \
		$(PROTO_PATH)/collector/collector.proto \
		$(PROTO_PATH)/target/target.proto

### update
##### update vendored source and regenerate python source
.PHONY: update
update: | update/vendor update/proto update/proto/legacy
	@echo "Update completed successfully"
