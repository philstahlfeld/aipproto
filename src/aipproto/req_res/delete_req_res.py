from typing import List
from aipproto import options, render, resource


def from_resource(resource_type: resource.Resource) -> List[render.ReqRes]:
    pascal = resource_type.format_type("pascal")
    return [
        render.ReqRes(
            type=f"Delete{pascal}Request",
            fields=[
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
            ],
        ),
    ]
