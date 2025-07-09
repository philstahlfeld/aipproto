from typing import List, Sequence

from aipproto import resource
from aipproto._internal import hierarchy, method_group, render
from aipproto._internal.req_res import (
    create_req_res,
    custom_req_res,
    delete_req_res,
    get_req_res,
    list_req_res,
    update_req_res,
)


def generate_file_content(
    package: str,
    service_name: str,
    resource_types: Sequence[resource.Resource],
    java_outer_classname: str = "TODO",
) -> str:
    """Generates the content of a proto file based on the provided resources.

    Args:
        package: The proto package (e.g. "foo.bar.v1").
        service_name: The name of the service (e.g. "BarService").
        resource_types: The resource types in the API.
    """
    method_groups = [
        method_group.from_resource(resource_type) for resource_type in resource_types
    ]

    resources = [
        render.Resource(
            type=rt.format_type("pascal"),
            pattern=hierarchy.pattern(rt),
            domain=rt.namespace().name,
            singular=rt.format_type("camel"),
            plural=rt.format_type("camel", "pl"),
        )
        for rt in resource_types
    ]

    req_res = []
    for resource_type in resource_types:
        req_res.extend(_make_req_res(resource_type))

    fspec = render.FileSpec(
        package=package,
        service_name=service_name,
        method_groups=method_groups,
        imports=_IMPORTS,
        resources=resources,
        req_res=req_res,
        java_outer_classname=java_outer_classname,
    )

    return fspec.render()


def _make_req_res(resource_type: resource.Resource) -> List[render.ReqRes]:
    req_res = []
    for fn in _REQ_RES_FNS:
        req_res.extend(fn(resource_type))
    for method in resource_type.config().custom_methods:
        req_res.extend(custom_req_res.from_resource(resource_type, method))
    return req_res


_REQ_RES_FNS = [
    get_req_res.from_resource,
    list_req_res.from_resource,
    create_req_res.from_resource,
    update_req_res.from_resource,
    delete_req_res.from_resource,
]

_IMPORTS = [
    "google/api/annotations.proto",
    "google/api/client.proto",
    "google/api/field_behavior.proto",
    "google/api/resource.proto",
    "google/protobuf/empty.proto",
    "google/protobuf/field_mask.proto",
]
