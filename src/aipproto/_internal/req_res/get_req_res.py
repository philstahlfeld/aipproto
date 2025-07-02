from typing import List
from aipproto import resource
from aipproto._internal import options, render


def from_resource(resource_type: resource.Resource) -> List[render.ReqRes]:
    pascal = resource_type.format_type("pascal")
    return [
        render.ReqRes(
            type=f"Get{resource_type.format_type('pascal')}Request",
            description=f"Request message for retrieving a {pascal}.",
            fields=[
                render.ReqResField(
                    type="string",
                    name="name",
                    comment_lines=[
                        f"The name of the {pascal} to retrieve.",
                    ],
                    options=[
                        options.field_behavior("REQUIRED"),
                        options.resource_reference(
                            "type", f"{resource_type.namespace().name}/{pascal}"
                        ),
                    ],
                ),
            ],
        ),
    ]
