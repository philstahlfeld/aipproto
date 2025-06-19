import importlib
import importlib.resources
from typing import List, NamedTuple

import jinja2


class FileSpec(NamedTuple):
    package: str
    domain: str
    service_name: str
    method_groups: List["MethodGroup"] = []
    imports: List[str] = []
    resources: List["Resource"] = []

    def render(self) -> str:
        template_path = importlib.resources.files("aipproto") / "templates"
        loader = jinja2.FileSystemLoader(str(template_path))
        env = jinja2.Environment(loader=loader)
        template = env.get_template("proto.jinja")
        return template.render(spec=self)


class MethodGroup(NamedTuple):
    type: str
    methods: List["Method"]


class Method(NamedTuple):
    name: str
    request_type: str
    response_type: str
    options: List["Option"] = []


class Option(NamedTuple):
    type: str
    value: str

class Resource(NamedTuple):
    type: str
    pattern: str
