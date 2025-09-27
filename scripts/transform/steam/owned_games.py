import polars as pl

import core.dataset.bronze.steam
import core.dataset.silver.steam
from core.dataset.bronze import BronzeDataset
from core.dataset.silver import SilverDataset
from scripts.transform import Transform


class TransformSteamOwnedGames(Transform):
    @property
    def input_dataset(self) -> BronzeDataset:
        return core.dataset.bronze.steam.owned_games

    @property
    def output_dataset(self) -> SilverDataset:
        return core.dataset.silver.steam.owned_games

    @property
    def mapping(self) -> dict[str, str]:
        return {
            "appid": "id",
            "playtime_forever": "playtime",
            "content_descriptorids": "tag",
        }

    def run(self) -> None:
        self.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            self.read_parquet()
            .rename(self.mapping)
            .explode("tag")
            .with_columns(
                pl.col(
                    "id",
                    "tag",
                ).cast(pl.String)
            )
            .select(self.output_dataset.schema.columns.keys())
        )


if __name__ == "__main__":
    TransformSteamOwnedGames().run()
