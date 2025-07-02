from aipproto import resource
from aipproto._internal import hierarchy, options, render


def from_resource(resource_type: resource.Resource) -> render.Method:
    pascal = resource_type.format_type("pascal")
    return render.Method(
        name=f"Create{pascal}",
        description=f"Creates a new {pascal}.",
        request_type=f"Create{pascal}Request",
        response_type=pascal,
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
    sig = (
        f"parent,{field},{field}_id"
        if resource_type.parent()
        else f"{field},{field}_id"
    )
    return options.method_signature(sig)
