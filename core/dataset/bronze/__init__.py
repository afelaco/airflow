from pandera.polars import DataFrameSchema

from core.dataset import Dataset


class BronzeDataset(Dataset):
    def __init__(
        self,
        container: str,
        name: str,
        schema: DataFrameSchema,
    ):
        super().__init__(
            storage_account="homeautobronzesa",
            container=container,
            name=name,
            schema=schema,
        )

    def get_path(self) -> str:
        return f"{self.container}/{self.name}.parquet"
