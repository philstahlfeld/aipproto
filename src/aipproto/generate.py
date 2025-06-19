from typing import Sequence

from aipproto import method_group, render, resource


def generate_file_content(
    package: str,
    service_name: str,
    resource_types: Sequence[resource.Resource],
) -> str:
    method_groups = [
        method_group.from_resource(resource_type) for resource_type in resource_types
    ]

    fspec = render.FileSpec(
        package=package,
        service_name=service_name,
        method_groups=method_groups,
        imports=["google/api/annotations.proto"],
    )

    return fspec.render()
