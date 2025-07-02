from typing import Literal, Optional

from aipproto._internal import render


def method_signature(signature: str) -> render.Option:
    return render.Option(
        type="google.api.method_signature",
        value=f'"{signature}"',
    )


def http(method: str, path: str, body: Optional[str] = None) -> render.Option:
    value = "{\n"
    value += f'      {method} : "{path}"\n'
    if body:
        value += f'      body: "{body}"\n'
    value += "    }"
    return render.Option(
        type="google.api.http",
        value=value,
    )


FieldBehavior = (
    Literal["IDENTIFIER"]
    | Literal["OUTPUT_ONLY"]
    | Literal["REQUIRED"]
    | Literal["OPTIONAL"]
)


def field_behavior(behavior: FieldBehavior) -> render.Option:
    return render.Option(
        type="google.api.field_behavior",
        value=f"{behavior}",
    )


def resource_reference(specifier: str, type: str) -> render.Option:
    value = "{\n"
    value += f'      {specifier}: "{type}"\n'
    value += "    }"
    return render.Option(
        type="google.api.resource_reference",
        value=value,
    )
