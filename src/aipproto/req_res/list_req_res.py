from typing import List
from aipproto import options, render, resource


def from_resource(resource_type: resource.Resource) -> List[render.ReqRes]:
    pascal_s = resource_type.format_type("pascal")
    pascal_pl = resource_type.format_type("pascal", "pl")
    return [
        render.ReqRes(
            type=f"List{pascal_pl}Request",
            fields=_request_fields(resource_type),
        ),
        render.ReqRes(
            type=f"List{pascal_pl}Response",
            fields=[
                render.ReqResField(
                    type=f"repeated {pascal_s}",
                    name=resource_type.format_type("snake", "pl"),
                ),
                render.ReqResField(
                    type="string",
                    name="next_page_token",
                ),
            ],
        ),
    ]


def _request_fields(resource_type: resource.Resource) -> List[render.ReqResField]:
    pascal = resource_type.format_type("pascal")
    fields = []
    if resource_type.parent():
        fields.append(
            render.ReqResField(
                type="string",
                name="parent",
                comment_lines=[
                    f"The parent that owns this collection of {pascal}.",
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
                type="int32",
                name="page_size",
            ),
            render.ReqResField(
                type="string",
                name="page_token",
            ),
        ]
    )
    return fields
