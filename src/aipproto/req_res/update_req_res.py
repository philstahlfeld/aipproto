from typing import List
from aipproto import options, render, resource


def from_resource(resource_type: resource.Resource) -> List[render.ReqRes]:
    pascal = resource_type.format_type("pascal")
    return [
        render.ReqRes(
            type=f"Update{pascal}Request",
            fields=_fields(resource_type),
        ),
    ]


def _fields(resource_type: resource.Resource) -> List[render.ReqResField]:
    pascal = resource_type.format_type("pascal")
    fields = [
        render.ReqResField(
            type=resource_type.format_type("pascal"),
            name=resource_type.format_type("snake"),
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
                options=[
                    options.field_behavior("OPTIONAL"),
                ],
            )
        )
    return fields
