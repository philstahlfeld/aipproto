from aipproto import resource
from aipproto._internal import hierarchy, options, render


def from_resource(resource_type: resource.Resource) -> render.Method:
    matcher = hierarchy.matcher(resource_type)
    return render.Method(
        name=f"Get{resource_type.format_type('pascal')}",
        description=f"Retrieves a {resource_type.format_type('pascal')}.",
        request_type=f"Get{resource_type.format_type('pascal')}Request",
        response_type=resource_type.format_type("pascal"),
        options=[
            options.http("get", f"/v1/{{name={matcher}}}"),
            options.method_signature("name"),
        ],
    )
