from core.api.response_model.steam.owned_games import SteamOwnedGamesApiResponseModel
from core.endpoint import Endpoint


owned_games = Endpoint(
    url="IPlayerService/GetOwnedGames/v1/",
    response_model=SteamOwnedGamesApiResponseModel,
)
