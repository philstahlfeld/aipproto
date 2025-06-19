from typing import Optional

from aipproto import render


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
