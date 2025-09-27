from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

from pandera.polars import DataFrameSchema


@dataclass
class Dataset(ABC):
    name: str
    schema: DataFrameSchema
    container: str
    storage_account: Literal[
        "homeautobronzesa",
        "homeautosilversa",
        "homeautogoldsa",
    ]

    @abstractmethod
    def get_path(self) -> str:
        pass
