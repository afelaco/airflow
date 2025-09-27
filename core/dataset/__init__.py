from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

from pandera.polars import DataFrameSchema
import polars as pl

from core.logger import get_logger

logger = get_logger(name=__name__)


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
    storage_account_key: str

    @abstractmethod
    def get_path(self) -> str:
        pass

    def get_storage_options(self) -> dict:
        return {
            "account_name": self.storage_account,
            "account_key": self.storage_account_key,
        }

    def read_parquet(self) -> pl.DataFrame:
        source = self.get_path()
        df = pl.read_parquet(
            source=source,
            storage_options=self.get_storage_options(),
        ).pipe(self.schema.validate)

        logger.info("%s records read from %s", len(df), source)

        return df

    def write_parquet(self, df: pl.DataFrame) -> None:
        file = self.get_path()
        df.pipe(self.schema.validate).write_parquet(
            file=file,
            storage_options=self.get_storage_options(),
        )

        logger.info("%s records written to %s", len(df), file)
