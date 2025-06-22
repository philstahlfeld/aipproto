from typing import List, Sequence

from aipproto import hierarchy, method_group, render, resource
from aipproto.req_res import (
    create_req_res,
    delete_req_res,
    get_req_res,
    list_req_res,
    update_req_res,
)


def generate_file_content(
    package: str,
    service_name: str,
    resource_types: Sequence[resource.Resource],
) -> str:
    method_groups = [
        method_group.from_resource(resource_type) for resource_type in resource_types
    ]

    resources = [
        render.Resource(
            type=rt.format_type("pascal"),
            pattern=hierarchy.pattern(rt),
            domain=rt.namespace().name,
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
        imports=["google/api/annotations.proto"],
        resources=resources,
        req_res=req_res,
    )

    return fspec.render()


def _make_req_res(resource_type: resource.Resource) -> List[render.ReqRes]:
    req_res = []
    for fn in _REQ_RES_FNS:
        req_res.extend(fn(resource_type))
    return req_res


_REQ_RES_FNS = [
    get_req_res.from_resource,
    list_req_res.from_resource,
    create_req_res.from_resource,
    update_req_res.from_resource,
    delete_req_res.from_resource,
]
