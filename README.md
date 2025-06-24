# aipproto
__TL;DR - Helper for generating [AIP](https://aip.dev) proto files.__

The AIPs are a wonderful style guide for building APIs. However, AIP compliant proto files are a bit cumbersome to create and maintain. This python package makes it easy to define hierarchies of AIP resources and then generate the corresponding proto files that define the AIP APIs for those resources.

## Installation
```sh
pip install aipproto
```

## Usage
```py
import aipproto

# Define the resource hierarchy for your API.
namespace = aipproto.Namespace("api.domain.com")
foo = namespace.resource("Foo")
bar = foo.nest("Bar")

# Generate the proto content.
content = aipproto.generate_file_content(
    package="domain.api.v1",
    service_name="TestService",
    resource_types=[foo, bar],
)

# Save it to a file.
with open("domain/api/v1/service.autogen.proto", "w") as f:
    f.write(content)
```
If this documentation is out of date, check out `tests/test_generate.py` or other tests in the `tests/` directory. 

## Conformance testing
To ensure that this package generates protos that conform to the AIP definitions, we run the [api-linter](https://linter.aip.dev/) on the generated proto files.

The following command is used to run the tests:
```
pytest && \
bazel build tests/testdata/v1:golden_proto_descriptor_set && \
api-linter --descriptor-set-in bazel-bin/tests/testdata/v1/golden_proto_descriptor_set.pb tests/testdata/v1/golden.proto --output-format github
```