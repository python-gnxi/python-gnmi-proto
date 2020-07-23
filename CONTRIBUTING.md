# Contribution Guide

## Developer Documentation
### Regenerating Protobuf Source
The project uses a git submodule under the [vendor directory](vendor/github.com/openconfig/gnmi) to keep proto files in
sync with upstream. You can update the module and regenerate the related source using `make`.

```sh
make update
```

### gNMI Target Server
You can use the [google/gnxi/gnmi_target](https://github.com/google/gnxi/tree/master/gnmi_target) to test the client 
code. You can set this up using the the following commands (assuming you have ``golang` and `GOPATH` configured 
correctly).

#### Installation
```sh
# install the shell binary  
go get -u github.com/google/gnxi/gnmi_target
go install -v github.com/google/gnxi/gnmi_target
```
#### Sample Configuration
You can use the configuration provided at [tests/integration/fixtures/config.json](tests/integration/fixtures/config.json) 
or fetch it using curl.

```sh
# fetch test configuration from github
curl -sLO https://raw.githubusercontent.com/python-gnxi/python-gnmi-proto/master/tests/integration/fixtures/config.json
```

Once you have a configuration you can start the server like shown below.
```sh
# run server
gnmi_target \
    -bind_address ":9339" \
    -username admin \
    -password secret \
    -logtostderr \
    -notls \
    -config tests/integration/fixtures/config.json
```
