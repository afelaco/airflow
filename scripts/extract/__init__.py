from abc import ABC, abstractmethod
import polars as pl
from core.api.client import ApiClient
from core.dataset import Dataset
from core.endpoint import Endpoint

from core.logger import get_logger
from core.utils import get_secret

logger = get_logger(name=__name__)


class Extract(ABC):
    @property
    @abstractmethod
    def api_client(self) -> ApiClient:
        pass

    @property
    @abstractmethod
    def endpoint(self) -> Endpoint:
        pass

    @property
    @abstractmethod
    def dataset(self) -> Dataset:
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def get_data(self) -> pl.DataFrame:
        pass

    def write_parquet(self, df: pl.DataFrame) -> None:
        container_name = self.dataset.container
        blob_path = self.dataset.get_path()
        path = f"abfss://{container_name}/{blob_path}"

        storage_options = {
            "account_name": "homeautosa",
            "account_key": get_secret("AZURE-STORAGE-ACCOUNT-KEY"),
        }

        df.write_parquet(
            path,
            storage_options=storage_options,
        )

        logger.info(
            "%s records written to %s",
            len(df),
            path,
        )
