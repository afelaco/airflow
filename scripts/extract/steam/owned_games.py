import polars as pl

import core.dataset.steam
from core.dataset.steam import SteamDataset
from core.endpoint.steam import SteamEndpoint
from scripts.extract.steam import ExtractSteam


class ExtractSteamOwnedGames(ExtractSteam):
    @property
    def endpoint(self) -> SteamEndpoint:
        return core.endpoint.steam.owned_games

    @property
    def dataset(self) -> SteamDataset:
        return core.dataset.steam.owned_games

    def run(self) -> None:
        self.write_parquet(df=self.get_data())

    def get_data(self) -> pl.DataFrame:
        params = {"include_appinfo": "true"}
        data = self.api_client.get(
            endpoint=self.endpoint,
            params=params,
        )
        return pl.DataFrame(data=data).pipe(self.dataset.schema.validate)


if __name__ == "__main__":
    data = (
        ExtractSteamOwnedGames().get_data().explode("content_descriptorids").to_pandas()
    )
