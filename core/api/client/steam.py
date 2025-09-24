from core.api.authentication.api_key import ApiKeyAuthentication
from core.api.client import ApiClient
from core.config import settings

from core.endpoint import Endpoint


class SteamApiClient(ApiClient, ApiKeyAuthentication):
    def __init__(self) -> None:
        ApiClient.__init__(self)
        ApiKeyAuthentication.__init__(self, api_key=settings.steam_api_key)

    def get(self, endpoint: Endpoint, params: dict[str, str]) -> list[dict]:
        data: list = []
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
        return data
        # data = []
        # page = 0
        # page_size = 100
        # url = self.get_url(endpoint_url=endpoint.url)
        # while True:
        #     params = {
        #         "count": page_size,
        #         "offset": page * page_size,
        #     }
        #     headers = self.get_auth_headers()
        #     response = self.session.get(
        #         url=url,
        #         params=params,
        #         headers=headers,
        #         timeout=120,
        #     )
        #     response.raise_for_status()
        #     batch = endpoint.response_model.model_validate_json(
        #         response.content
        #     ).model_dump(by_alias=True)
        #     if not batch:
        #         break
        #     data.extend(batch)
        #     logger.info("%s records read from %s", len(data), response.url)
        #     page += 1
        # return data

    def get_auth_headers(self) -> dict[str, str]:
        return {"x-webapi-key": self.api_key}
