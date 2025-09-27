from dataclasses import dataclass
from typing import Literal

from core.dataset import Dataset


@dataclass
class BronzeDataset(Dataset):
    storage_account: Literal["homeautobronzesa"] = "homeautobronzesa"

    def get_path(self) -> str:
        return f"{self.container}/{self.name}.parquet"
