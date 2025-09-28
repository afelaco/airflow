from pandera.polars import DataFrameSchema, Column

from core.dataset.bronze import BronzeDataset

owned_games = BronzeDataset(
    container="steam",
    name="owned-games",
    schema=DataFrameSchema(
        {
            "appid": Column(int),
            "name": Column(str),
            "playtime_forever": Column(int),
            "content_descriptorids": Column(list[int], nullable=True),
        }
    ),
)
player_achievements = BronzeDataset(
    container="steam",
    name="player-achievements",
    schema=DataFrameSchema(
        {
            "appid": Column(int),
            "name": Column(str),
            "playtime_forever": Column(int),
            "content_descriptorids": Column(list[int], nullable=True),
        }
    ),
)
