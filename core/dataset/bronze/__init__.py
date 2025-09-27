from dataclasses import dataclass
from typing import Literal

from core.dataset import Dataset
from core.utils import get_secret


@dataclass
class BronzeDataset(Dataset):
    storage_account: Literal["homeautobronzesa"] = "homeautobronzesa"
    storage_account_key: str = get_secret("BRONZE-LAYER-KEY")

    def get_path(self) -> str:
        return f"abfss://{self.container}/{self.name}.parquet"
