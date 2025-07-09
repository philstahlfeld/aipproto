from aipproto import resource, resource_config
from aipproto._internal import hierarchy, options, render


def from_resource(
    resource_type: resource.Resource,
    method: resource_config.CustomMethod,
) -> render.Method:
    pascal = resource_type.format_type(
        "pascal", number="pl" if method.collection_based else "s"
    )
    return render.Method(
        name=f"{method.name}{pascal}",
        description=f"TODO: describe custom method.",
        request_type=f"{method.name}{pascal}Request",
        response_type=f"{method.name}{pascal}Response",
        options=[
            _http(resource_type, method),
        ],
    )


def _http(
    resource_type: resource.Resource, method: resource_config.CustomMethod
) -> render.Option:
    if not method.name:
        raise ValueError("Custom method name cannot be empty.")
    method_camel = method.name[:1].lower() + method.name[1:]
    if method.collection_based:
        parent = resource_type.parent()
        if parent:
            path = f"/v1/{{parent={hierarchy.matcher(parent)}}}/{resource_type.collection()}:{method_camel}"
        else:
            path = f"/v1/{resource_type.collection()}:{method_camel}"
    else:
        path = f"/v1/{{name={hierarchy.matcher(resource_type)}}}:{method_camel}"
    return options.http("post", path, body="*")
