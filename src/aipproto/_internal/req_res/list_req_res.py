from typing import List
from aipproto import resource
from aipproto._internal import options, render


def from_resource(resource_type: resource.Resource) -> List[render.ReqRes]:
    pascal_s = resource_type.format_type("pascal")
    pascal_pl = resource_type.format_type("pascal", "pl")
    return [
        render.ReqRes(
            type=f"List{pascal_pl}Request",
            description=f"Request message for listing {pascal_pl}.",
            fields=_request_fields(resource_type),
        ),
        render.ReqRes(
            type=f"List{pascal_pl}Response",
            description=f"Response message for listing {pascal_pl}.",
            fields=[
                render.ReqResField(
                    type=f"repeated {pascal_s}",
                    name=resource_type.format_type("snake", "pl"),
                    comment_lines=[
                        f"The list of {pascal_pl} in the collection.",
                    ],
                ),
                render.ReqResField(
                    type="string",
                    name="next_page_token",
                    comment_lines=[
                        f"The token to use for the next page of results.",
                    ],
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
                comment_lines=[
                    f"The maximum number of {pascal} to return.",
                ],
                options=[
                    options.field_behavior("OPTIONAL"),
                ],
            ),
            render.ReqResField(
                type="string",
                name="page_token",
                comment_lines=[
                    f"The page token to use for the next page of results.",
                ],
                options=[
                    options.field_behavior("OPTIONAL"),
                ],
            ),
        ]
    )
    return fields
