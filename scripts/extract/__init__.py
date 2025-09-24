from abc import ABC, abstractmethod
import polars as pl
from core.api.client import ApiClient
from core.dataset import Dataset
from core.endpoint import Endpoint


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

    # def write_data(self, data: pyspark.sql.DataFrame, path: str) -> None:
    #     self.validate_schema(
    #         data=data,
    #         schema=self.dataset.schema,
    #     )
    #     LandingZone().write_parquet(
    #         df=data,
    #         container=self.dataset.container,
    #         path=path,
    #     )

    # @staticmethod
    # def validate_schema(data: pyspark.sql.DataFrame, schema: dict) -> None:
    #     if dict(data.schema) != schema:
    #         error = f"Schema mismatch!\nExpected: {schema}\nActual: {data.schema}"
    #         raise ValueError(error)
