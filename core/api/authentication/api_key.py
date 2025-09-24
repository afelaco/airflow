class ApiKeyAuthentication:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_auth_headers(self) -> dict[str, str]:
        return {"Authorization": f"Token {self.api_key}"}
