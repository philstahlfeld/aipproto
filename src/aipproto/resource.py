import re
from typing import Literal, NamedTuple, Optional

from aipproto import resource_config


class Namespace(NamedTuple):
    """A namespace for AIP resource types.

    Attributes:
        name: The name of the namepace (e.g. foo.yourdomain.com).
    """

    name: str
    default_config: Optional[resource_config.ResourceConfig] = None

    def resource(self, *args, **kwargs) -> "Resource":
        """Create a new Resource in this namespace."""
        return Resource(self, None, *args, **kwargs)


class Resource:
    def __init__(
        self,
        namespace: Namespace,
        parent: Optional["Resource"],
        singular: str,
        plural: Optional[str] = None,
        config: Optional[resource_config.ResourceConfig] = None,
    ):
        """Create a new Resource.

        Args:
            namespace: The namespace this resource belongs to.
            singular: The singular name of the resource (e.g. "foo").
            plural: The plural name of the resource (e.g. "foos"). If not provided,
                it defaults to the singular name with an 's' appended.
            parent: An optional parent resource, if this is a nested resource.
        """
        self._namespace = namespace
        self._parent = parent
        self._singular = singular
        self._plural = plural or singular + "s"
        self._config = config
        self.has_children = False

    def nest(self, *args, **kwargs) -> "Resource":
        """Create a new child Resource."""
        self.has_children = True
        return Resource(self._namespace, self, *args, **kwargs)

    def format_type(self, case: "Case", number: "Number" = "s") -> str:
        """Format the resource name according to the specified case and number."""
        base = self._singular if number == "s" else self._plural
        if case == "camel":
            return base[0].lower() + base[1:]
        elif case == "snake":
            return re.sub(r"(?<!^)(?=[A-Z])", "_", base).lower()
        elif case == "pascal":
            return base[0].upper() + base[1:]
        else:
            raise ValueError(f"Unknown case: {case}")

    def collection(self) -> str:
        return self.format_type("camel", "pl")

    def parent(self) -> Optional["Resource"]:
        """Get the parent resource, if any."""
        return self._parent

    def config(self) -> resource_config.ResourceConfig:
        return (
            self._config
            or self._namespace.default_config
            or resource_config.ResourceConfig()
        )

    def namespace(self) -> Namespace:
        """Get the namespace this resource belongs to."""
        return self._namespace


Case = Literal["camel", "snake", "pascal"]
Number = Literal["s", "pl"]
