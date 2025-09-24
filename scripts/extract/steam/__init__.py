from abc import ABC, abstractmethod
from core.api.client.steam import SteamApiClient

from core.dataset.steam import SteamDataset
from core.endpoint.steam import SteamEndpoint
from scripts.extract import Extract


class ExtractSteam(Extract, ABC):
    @property
    def api_client(self) -> SteamApiClient:
        return SteamApiClient()

    @property
    @abstractmethod
    def endpoint(self) -> SteamEndpoint:
        pass

    @property
    @abstractmethod
    def dataset(self) -> SteamDataset:
        pass
