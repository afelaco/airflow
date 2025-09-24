from abc import ABC, abstractmethod
from typing import Any

import requests


class ApiClient(ABC):
    def __init__(self) -> None:
        self.session = requests.Session()

    @abstractmethod
    def get(self, *args: Any, **kwargs: Any) -> list[dict[Any, Any]]:
        pass
