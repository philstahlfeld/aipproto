from aipproto import hierarchy, options, render, resource


def from_resource(resource_type: resource.Resource) -> render.Method:
    snake_s = resource_type.format_type("snake")
    return render.Method(
        name=f"Delete{resource_type.format_type('pascal')}",
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


def _method_signature(resource_type: resource.Resource) -> render.Option:
    fields = [resource_type.format_type("snake")]
    if resource_type.config().update_config().partial:
        fields.append("update_mask")
    return options.method_signature(",".join(fields))
