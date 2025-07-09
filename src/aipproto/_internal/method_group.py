from aipproto import resource
from aipproto._internal import render
from aipproto._internal.methods import (
    create_method,
    custom_method,
    delete_method,
    get_method,
    list_method,
    update_method,
)


def from_resource(resource_type: resource.Resource) -> render.MethodGroup:
    return render.MethodGroup(
        type=resource_type.format_type("pascal", "pl"),
        methods=[
            create_method.from_resource(resource_type),
            get_method.from_resource(resource_type),
            list_method.from_resource(resource_type),
            update_method.from_resource(resource_type),
            delete_method.from_resource(resource_type),
            *[
                custom_method.from_resource(resource_type, method)
                for method in resource_type.config().custom_methods
            ],
        ],
    )
