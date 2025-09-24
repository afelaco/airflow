from abc import ABC

from pydantic import BaseModel


class Endpoint(ABC):
    def __init__(self, url: str, response_model: type[BaseModel]):
        self.url = url
        self.response_model = response_model
