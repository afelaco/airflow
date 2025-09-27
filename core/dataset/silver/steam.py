from pandera.polars import DataFrameSchema, Column

from core.dataset.silver import SilverDataset

owned_games = SilverDataset(
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
