from abc import ABC, abstractmethod
from typing import Any


class Dataset(ABC):
    def __init__(
        self,
        name: str,
        container: str,
        schema: dict[str, Any],
    ):
        self.name = name
        self.container = container
        self.schema = schema

    @abstractmethod
    def get_path(self) -> str:
        pass
