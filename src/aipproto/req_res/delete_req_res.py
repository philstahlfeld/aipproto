from typing import List
from aipproto import options, render, resource


def from_resource(resource_type: resource.Resource) -> List[render.ReqRes]:
    pascal = resource_type.format_type("pascal")
    return [
        render.ReqRes(
            type=f"Delete{pascal}Request",
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
                name="name",
                comment_lines=[
                    f"The name of the {pascal} to delete.",
                ],
                options=[
                    options.field_behavior("REQUIRED"),
                    options.resource_reference(
                        "type", f"{resource_type.namespace().name}/{pascal}"
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
