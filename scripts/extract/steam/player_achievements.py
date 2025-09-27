import polars as pl

import core.dataset.bronze.steam
import core.endpoint.steam
from core.dataset.bronze import BronzeDataset
from core.endpoint import Endpoint
from scripts.extract.steam import ExtractSteam


class ExtractSteamPlayerAchievements(ExtractSteam):
    @property
    def endpoint(self) -> Endpoint:
        return core.endpoint.steam.owned_games

    @property
    def dataset(self) -> BronzeDataset:
        return core.dataset.bronze.steam.owned_games

    def run(self) -> None:
        self.dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        params = {"include_appinfo": "true"}
        data = self.api_client.get(
            endpoint=self.endpoint,
            params=params,
        )
        return pl.DataFrame(data=data).pipe(self.dataset.schema.validate)


if __name__ == "__main__":
    ExtractSteamPlayerAchievements().run()
