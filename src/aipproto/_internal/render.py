import importlib
import importlib.resources
from typing import List, NamedTuple

import jinja2


class FileSpec(NamedTuple):
    package: str
    service_name: str
    method_groups: List["MethodGroup"] = []
    imports: List[str] = []
    resources: List["Resource"] = []
    req_res: List["ReqRes"] = []
    java_outer_classname: str = "TODO"

    def render(self) -> str:
        template_path = (
            importlib.resources.files("aipproto") / "_internal" / "templates"
        )
        loader = jinja2.FileSystemLoader(str(template_path))
        env = jinja2.Environment(loader=loader)
        template = env.get_template("proto.jinja")
        return template.render(spec=self)


class MethodGroup(NamedTuple):
    type: str
    methods: List["Method"]


class Method(NamedTuple):
    name: str
    description: str
    request_type: str
    response_type: str
    options: List["Option"] = []


class Option(NamedTuple):
    type: str
    value: str


class Resource(NamedTuple):
    type: str
    pattern: str
    domain: str
    singular: str
    plural: str


class ReqResGroup(NamedTuple):
    req_res: List["ReqRes"]


class ReqRes(NamedTuple):
    type: str
    description: str
    fields: List["ReqResField"]


class ReqResField(NamedTuple):
    type: str
    name: str
    comment_lines: List[str] = []
    options: List[Option] = []
