from pandera.polars import DataFrameSchema, Column

from core.dataset.gold import GoldDataset

dim_owned_games = GoldDataset(
    container="steam",
    name="dim-owned-games",
    schema=DataFrameSchema(
        {
            "id": Column(str, unique=True),
            "name": Column(str),
            "playtime": Column(int),
        }
    ),
)
fact_owned_games_tags = GoldDataset(
    container="steam",
    name="fact-owned-games-tags",
    schema=DataFrameSchema(
        {
            "id": Column(str),
            "tag": Column(str),
        }
    ),
)
