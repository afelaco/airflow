from abc import ABC, abstractmethod

from pandera.polars import DataFrameSchema


class Dataset(ABC):
    def __init__(
        self,
        name: str,
        container: str,
        schema: DataFrameSchema,
    ):
        self.name = name
        self.container = container
        self.schema = schema

    @abstractmethod
    def get_path(self) -> str:
        pass
