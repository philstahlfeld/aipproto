from typing import List
from aipproto import resource, resource_config
from aipproto._internal import options, render


def from_resource(
    resource_type: resource.Resource,
    method: resource_config.CustomMethod,
) -> List[render.ReqRes]:
    pascal = resource_type.format_type(
        "pascal", number="pl" if method.collection_based else "s"
    )
    return [
        render.ReqRes(
            type=f"{method.name}{pascal}Request",
            description=f"TODO: describe custom method request.",
            fields=_fields(resource_type, method),
        ),
        render.ReqRes(
            type=f"{method.name}{pascal}Response",
            description=f"TODO: describe custom method response.",
            fields=[],
        ),
    ]


def _fields(
    resource_type: resource.Resource, method: resource_config.CustomMethod
) -> List[render.ReqResField]:
    pascal = resource_type.format_type(
        "pascal", number="pl" if method.collection_based else "s"
    )
    pascal_s = resource_type.format_type("pascal")
    if method.collection_based:
        return [
            render.ReqResField(
                type="string",
                name="parent",
                comment_lines=[
                    f"The parent that owns this collection of {pascal}.",
                ],
                options=[
                    options.field_behavior("REQUIRED"),
                    options.resource_reference(
                        "child_type", f"{resource_type.namespace().name}/{pascal_s}"
                    ),
                ],
            )
        ]
    return [
        render.ReqResField(
            type="string",
            name="name",
            comment_lines=[
                f"The name of the {pascal}.",
            ],
            options=[
                options.field_behavior("REQUIRED"),
                options.resource_reference(
                    "type", f"{resource_type.namespace().name}/{pascal}"
                ),
            ],
        ),
    ]
