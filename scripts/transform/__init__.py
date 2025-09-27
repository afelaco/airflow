from abc import ABC, abstractmethod

import polars as pl

from core.dataset.bronze import BronzeDataset
from core.dataset.silver import SilverDataset
from core.logger import get_logger
from core.utils import get_secret

logger = get_logger(name=__name__)


class Transform(ABC):
    @property
    @abstractmethod
    def input_dataset(self) -> BronzeDataset:
        pass

    @property
    @abstractmethod
    def output_dataset(self) -> SilverDataset:
        pass

    @property
    @abstractmethod
    def mapping(self) -> dict[str, str]:
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def get_data(self) -> pl.DataFrame:
        pass

    def read_parquet(self) -> pl.DataFrame:
        source = f"abfss://{self.input_dataset.get_path()}"
        storage_options = {
            "account_name": "homeautobronzesa",
            "account_key": get_secret("BRONZE-LAYER-KEY"),
        }
        df = pl.read_parquet(
            source=source,
            storage_options=storage_options,
        ).pipe(self.input_dataset.schema.validate)

        logger.info(
            "%s records read from %s",
            len(df),
            source,
        )

        return df

    def write_parquet(self, df: pl.DataFrame) -> None:
        file = f"abfss://{self.output_dataset.get_path()}"
        storage_options = {
            "account_name": "homeautosilversa",
            "account_key": get_secret("SILVER-LAYER-KEY"),
        }
        df.pipe(self.output_dataset.schema.validate).write_parquet(
            file=file,
            storage_options=storage_options,
        )

        logger.info(
            "%s records written to %s",
            len(df),
            file,
        )
