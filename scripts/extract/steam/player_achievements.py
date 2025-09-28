import polars as pl

import core.dataset.bronze.steam
import core.dataset.gold.steam
import core.endpoint.steam
from core.dataset.bronze import BronzeDataset
from core.endpoint import Endpoint
from core.logger import get_logger
from scripts.extract.steam import ExtractSteam


logger = get_logger(name=__name__)


class ExtractSteamPlayerAchievements(ExtractSteam):
    @property
    def endpoint(self) -> Endpoint:
        return core.endpoint.steam.player_achievements

    @property
    def dataset(self) -> BronzeDataset:
        return core.dataset.bronze.steam.player_achievements

    def run(self) -> None:
        self.dataset.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        data = []
        played_games = self.get_played_games()
        for id in played_games["id"]:
            try:
                data.extend(
                    self.api_client.get(
                        endpoint=self.endpoint,
                        params={"appid": id},
                    )
                )
            except Exception:
                continue
        return pl.DataFrame(data=data)

    @staticmethod
    def get_played_games() -> pl.DataFrame:
        return core.dataset.gold.steam.dim_owned_games.read_parquet().filter(
            pl.col("playtime") > 0
        )


if __name__ == "__main__":
    data = ExtractSteamPlayerAchievements().get_data()
