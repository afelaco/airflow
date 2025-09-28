import polars as pl

import core.dataset.gold.steam
import core.dataset.silver.steam
from core.dataset.gold import GoldDataset
from scripts.load import Load


class LoadFactOwnedGamesTags(Load):
    @property
    def output_dataset(self) -> GoldDataset:
        return core.dataset.gold.steam.fact_owned_games_tags

    def run(self) -> None:
        self.output_dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        return (
            core.dataset.silver.steam.owned_games.read_parquet()
            .filter(pl.col("tag").is_not_null())
            .select(self.output_dataset.schema.columns.keys())
        )


if __name__ == "__main__":
    LoadFactOwnedGamesTags().run()
