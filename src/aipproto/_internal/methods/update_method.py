from aipproto import resource
from aipproto._internal import hierarchy, options, render


def from_resource(resource_type: resource.Resource) -> render.Method:
    snake_s = resource_type.format_type("snake")
    return render.Method(
        name=f"Update{resource_type.format_type('pascal')}",
        description=f"Updates a {resource_type.format_type('pascal')}.",
        request_type=f"Update{resource_type.format_type('pascal')}Request",
        response_type=resource_type.format_type("pascal"),
        options=[
            options.http(
                "patch",
                f"/v1/{{{snake_s}.name={hierarchy.matcher(resource_type)}}}",
                body=snake_s,
            ),
            _method_signature(resource_type),
        ],
    )


def _method_signature(resource_type: resource.Resource) -> render.Option:
    fields = [resource_type.format_type("snake")]
    if resource_type.config().update_config().partial:
        fields.append("update_mask")
    return options.method_signature(",".join(fields))
