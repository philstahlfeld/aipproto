from typing import List
from aipproto import options, render, resource


def from_resource(resource_type: resource.Resource) -> List[render.ReqRes]:
    pascal = resource_type.format_type("pascal")
    return [
        render.ReqRes(
            type=f"Create{pascal}Request",
            fields=_fields(resource_type),
        ),
    ]


def _fields(resource_type: resource.Resource) -> List[render.ReqResField]:
    pascal = resource_type.format_type("pascal")
    fields = []
    if resource_type.parent():
        fields.append(
            render.ReqResField(
                type="string",
                name="parent",
                comment_lines=[
                    f"The parent that owns this {pascal}.",
                ],
                options=[
                    options.field_behavior("IDENTIFIER"),
                    options.resource_reference(
                        "child_type", f"{resource_type.namespace().name}/{pascal}"
                    ),
                ],
            )
        )
    fields.extend(
        [
            render.ReqResField(
                type="string",
                name=f"{resource_type.format_type('snake')}_id",
            ),
            render.ReqResField(
                type=resource_type.format_type("pascal"),
                name=resource_type.format_type("snake"),
            ),
        ]
    )
    return fields
