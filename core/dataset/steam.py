from pandera.polars import DataFrameSchema, Column

from core.dataset import Dataset


class SteamDataset(Dataset):
    def __init__(
        self,
        name: str,
        schema: DataFrameSchema,
    ):
        super().__init__(
            name=name,
            container="steam",
            schema=schema,
        )

    def get_path(self) -> str:
        return f"{self.name}.parquet"


owned_games = SteamDataset(
    name="owned_games",
    schema=DataFrameSchema(
        {
            "appid": Column(int),
            "name": Column(str),
            "playtime_forever": Column(int),
            "content_descriptorids": Column(list[int], nullable=True),
        }
    ),
)
