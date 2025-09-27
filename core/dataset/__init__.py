from abc import ABC, abstractmethod

from pandera.polars import DataFrameSchema


class Dataset(ABC):
    def __init__(
        self,
        storage_account: str,
        container: str,
        name: str,
        schema: DataFrameSchema,
    ):
        self.storage_account = storage_account
        self.container = container
        self.name = name
        self.schema = schema

    @abstractmethod
    def get_path(self) -> str:
        pass
