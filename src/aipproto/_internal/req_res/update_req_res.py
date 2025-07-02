from typing import List
from aipproto import resource
from aipproto._internal import options, render


def from_resource(resource_type: resource.Resource) -> List[render.ReqRes]:
    pascal = resource_type.format_type("pascal")
    return [
        render.ReqRes(
            type=f"Update{pascal}Request",
            description=f"Request message for updating a {pascal}.",
            fields=_fields(resource_type),
        ),
    ]


def _fields(resource_type: resource.Resource) -> List[render.ReqResField]:
    pascal = resource_type.format_type("pascal")
    fields = [
        render.ReqResField(
            type=resource_type.format_type("pascal"),
            name=resource_type.format_type("snake"),
            comment_lines=[
                f"The {pascal} being updated.",
            ],
            options=[
                options.field_behavior("REQUIRED"),
            ],
        )
    ]
    if resource_type.config().update_config().partial:
        fields.append(
            render.ReqResField(
                type="google.protobuf.FieldMask",
                name="update_mask",
                comment_lines=[
                    "The set of fields to update.",
                ],
                options=[
                    options.field_behavior("OPTIONAL"),
                ],
            )
        )
    return fields
