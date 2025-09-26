from abc import ABC, abstractmethod
import polars as pl
from core.api.client import ApiClient
from core.config import settings
from core.dataset import Dataset
from core.endpoint import Endpoint
from adlfs import AzureBlobFileSystem

from core.logger import get_logger

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
        # Declare Azure Blob Storage parameters
        storage_account_name = "homeautosa"
        container_name = self.dataset.container
        blob_path = self.dataset.get_path()

        # Create a filesystem object
        fs = AzureBlobFileSystem(
            account_name=storage_account_name,
            account_key=settings.azure_storage_account_key,
        )

        # Open the blob as a file-like object and write Parquet
        with fs.open(f"{container_name}/{blob_path}", "wb") as f:
            df.write_parquet(f)

        logger.info(
            "%s records written to %s/%s/%s",
            len(df),
            storage_account_name,
            container_name,
            blob_path,
        )

    # @staticmethod
    # def validate_schema(data: pyspark.sql.DataFrame, schema: dict) -> None:
    #     if dict(data.schema) != schema:
    #         error = f"Schema mismatch!\nExpected: {schema}\nActual: {data.schema}"
    #         raise ValueError(error)
