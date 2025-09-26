from core.api.authentication.api_key import ApiKeyAuthentication
from core.api.client import ApiClient
from core.config import settings

from core.endpoint import Endpoint
from core.logger import get_logger

logger = get_logger(name=__name__)


class SteamApiClient(ApiClient, ApiKeyAuthentication):
    def __init__(self) -> None:
        ApiClient.__init__(self)
        ApiKeyAuthentication.__init__(self, api_key=settings.steam_api_key)

    def get(self, endpoint: Endpoint, params: dict[str, str]) -> list[dict]:
        data: list = []
        params = params | {"steamid": settings.steam_id}
        response = self.session.get(
            url=endpoint.url,
            params=params,
            headers=self.get_auth_headers(),
        )
        response.raise_for_status()
        data.extend(
            endpoint.response_model.model_validate_json(response.content).model_dump(
                by_alias=True
            )
        )
        logger.info("%s records read from %s", len(data), response.url)

        return data

    def get_auth_headers(self) -> dict[str, str]:
        return {"x-webapi-key": self.api_key}
