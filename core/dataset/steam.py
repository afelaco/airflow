from typing import Any
from polars import String, Int64, List
from core.dataset import Dataset


class SteamDataset(Dataset):
    def __init__(
        self,
        name: str,
        schema: dict[str, Any],
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
    schema={
        "appid": Int64,
        "name": String,
        "playtime_forever": Int64,
        "content_descriptorids": List(Int64),
    },
)
