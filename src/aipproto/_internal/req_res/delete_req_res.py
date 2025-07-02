from typing import List
from aipproto import resource
from aipproto._internal import options, render


def from_resource(resource_type: resource.Resource) -> List[render.ReqRes]:
    pascal = resource_type.format_type("pascal")
    return [
        render.ReqRes(
            type=f"Delete{pascal}Request",
            description=f"Request message for deleting a {pascal}.",
            fields=_fields(resource_type),
        ),
    ]


def _fields(resource_type: resource.Resource) -> List[render.ReqResField]:
    pascal = resource_type.format_type("pascal")
    fields = [
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
    ]
    if resource_type.has_children:
        fields.append(
            render.ReqResField(
                type="bool",
                name="force",
                comment_lines=[
                    f"If set, deletes the {pascal} and all of its children.",
                ],
                options=[
                    options.field_behavior("OPTIONAL"),
                ],
            )
        )
    return fields
