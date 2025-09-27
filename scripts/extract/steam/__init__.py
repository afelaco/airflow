from abc import ABC

from core.api.client.steam import SteamApiClient
from scripts.extract import Extract


class ExtractSteam(Extract, ABC):
    @property
    def api_client(self) -> SteamApiClient:
        return SteamApiClient()
