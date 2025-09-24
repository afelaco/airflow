from core.api.response_model.steam.owned_games import SteamOwnedGamesApiResponseModel
from core.endpoint import Endpoint
from pydantic import BaseModel


class SteamEndpoint(Endpoint):
    BASE_URL = "https://api.steampowered.com/"

    def __init__(self, url: str, response_model: type[BaseModel]):
        super().__init__(
            url=self.BASE_URL,
            response_model=response_model,
        )
        self.url = self.BASE_URL + url


owned_games = SteamEndpoint(
    url="IPlayerService/GetOwnedGames/v1/",
    response_model=SteamOwnedGamesApiResponseModel,
)
