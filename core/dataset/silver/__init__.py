from dataclasses import dataclass
from typing import Literal

from core.dataset import Dataset
from core.utils import get_secret


@dataclass
class SilverDataset(Dataset):
    storage_account: Literal["homeautosilversa"] = "homeautosilversa"
    storage_account_key: str = get_secret("SILVER-LAYER-KEY")

    def get_path(self) -> str:
        return f"abfss://{self.container}/{self.name}.parquet"
