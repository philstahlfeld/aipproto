from typing import Sequence

from aipproto import hierarchy, method_group, render, resource


def generate_file_content(
    package: str,
    domain: str,
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
        )
        for rt in resource_types
    ]

    fspec = render.FileSpec(
        package=package,
        domain=domain,
        service_name=service_name,
        method_groups=method_groups,
        imports=["google/api/annotations.proto"],
        resources=resources,
    )

    return fspec.render()
