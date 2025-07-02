from aipproto import resource


def matcher(resource_type: resource.Resource) -> str:
    components = [resource_type.collection(), "*"]
    parent = resource_type.parent()
    while parent:
        current = parent
        components.insert(0, "*")
        components.insert(0, current.collection())
        parent = current.parent()
    return "/".join(components)


def pattern(resource_type: resource.Resource) -> str:
    components = [
        resource_type.collection(),
        f"{{{resource_type.format_type('snake')}}}",
    ]
    parent = resource_type.parent()
    while parent:
        current = parent
        components.insert(0, f"{{{current.format_type('snake')}}}")
        components.insert(0, current.collection())
        parent = current.parent()
    return "/".join(components)
