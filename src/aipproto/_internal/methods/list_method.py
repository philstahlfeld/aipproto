from aipproto import resource
from aipproto._internal import hierarchy, options, render


def from_resource(resource_type: resource.Resource) -> render.Method:
    return render.Method(
        name=f"List{resource_type.format_type('pascal', 'pl')}",
        description=f"Lists {resource_type.format_type('pascal', 'pl')}.",
        request_type=f"List{resource_type.format_type('pascal', 'pl')}Request",
        response_type=f"List{resource_type.format_type('pascal', 'pl')}Response",
        options=[
            _http(resource_type),
            _method_signature(resource_type),
        ],
    )


def _http(resource_type: resource.Resource) -> render.Option:
    camel_pl = resource_type.format_type("camel", "pl")
    parent = resource_type.parent()
    if not parent:
        return options.http("get", f"/v1/{camel_pl}")
    matcher = hierarchy.matcher(parent)
    return options.http("get", f"/v1/{{parent={matcher}}}/{camel_pl}")


def _method_signature(resource_type: resource.Resource) -> render.Option:
    sig = f"parent" if resource_type.parent() else ""
    return options.method_signature(sig)
