from aipproto import resource
from aipproto._internal import hierarchy, options, render


def from_resource(resource_type: resource.Resource) -> render.Method:
    return render.Method(
        name=f"Delete{resource_type.format_type('pascal')}",
        description=f"Deletes a {resource_type.format_type('pascal')}.",
        request_type=f"Delete{resource_type.format_type('pascal')}Request",
        response_type=_response_message(resource_type),
        options=[
            options.http(
                "delete",
                f"/v1/{{name={hierarchy.matcher(resource_type)}}}",
            ),
            options.method_signature("name"),
        ],
    )


def _response_message(resource_type: resource.Resource) -> str:
    if resource_type.config().delete_config().soft:
        return resource_type.format_type("pascal")
    return "google.protobuf.Empty"
