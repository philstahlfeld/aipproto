from aipproto import hierarchy, options, render, resource


def from_resource(resource_type: resource.Resource) -> render.Method:
    return render.Method(
        name=f"Create{resource_type.format_type('pascal')}",
        request_type=f"Create{resource_type.format_type('pascal')}Request",
        response_type=resource_type.format_type("pascal"),
        options=[
            _http(resource_type),
            _method_signature(resource_type),
        ],
    )


def _http(resource_type: resource.Resource) -> render.Option:
    field = resource_type.format_type("snake")
    collection = resource_type.collection()
    parent = resource_type.parent()
    if not parent:
        return options.http("post", f"/v1/{collection}", body=field)
    matcher = hierarchy.matcher(parent)
    return options.http("post", f"/v1/{{parent={matcher}}}/{collection}", body=field)


def _method_signature(resource_type: resource.Resource) -> render.Option:
    field = resource_type.format_type("snake")
    sig = f"parent,{field}" if resource_type.parent() else field
    return options.method_signature(sig)
