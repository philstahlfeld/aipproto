from typing import List, NamedTuple, Optional


class ResourceConfig:
    def __init__(
        self,
        update_config: Optional["UpdateConfig"] = None,
        delete_config: Optional["DeleteConfig"] = None,
        custom_methods: Optional[List["CustomMethod"]] = None,
    ):
        self._update_config = update_config
        self._delete_config = delete_config
        self.custom_methods = custom_methods or []

    def has_update_config(self) -> bool:
        return self._update_config is not None

    def update_config(self) -> "UpdateConfig":
        return self._update_config or UpdateConfig()

    def has_delete_config(self) -> bool:
        return self._delete_config is not None

    def delete_config(self) -> "DeleteConfig":
        return self._delete_config or DeleteConfig()


class UpdateConfig(NamedTuple):
    partial: bool = True


class DeleteConfig(NamedTuple):
    soft: bool = False


class CustomMethod(NamedTuple):
    name: str
    collection_based: bool = False
