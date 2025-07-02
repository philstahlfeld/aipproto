from typing import List
from aipproto import resource
from aipproto._internal import options, render


def from_resource(resource_type: resource.Resource) -> List[render.ReqRes]:
    pascal = resource_type.format_type("pascal")
    return [
        render.ReqRes(
            type=f"Create{pascal}Request",
            description=f"Request message for creating a {pascal}.",
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
                    options.field_behavior("REQUIRED"),
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
                comment_lines=[
                    f"The ID to use for the {pascal} being created.",
                ],
                options=[
                    options.field_behavior("OPTIONAL"),
                ],
            ),
            render.ReqResField(
                type=resource_type.format_type("pascal"),
                name=resource_type.format_type("snake"),
                comment_lines=[
                    f"The {pascal} being created.",
                ],
                options=[
                    options.field_behavior("REQUIRED"),
                ],
            ),
        ]
    )
    return fields
