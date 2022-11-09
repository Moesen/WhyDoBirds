from pathlib import Path
import pandas as pd
from src.data.birdcols import BirdColumns as BC
from src import data_processed_path
from abc import ABC, abstractmethod


class AbstractDataset(ABC):
    @abstractmethod
    def get_row(self) -> pd.Series:
        pass


class BirdDataset(AbstractDataset):
    def __init__(
        self,
        data_path: Path,
        cols: list[BC] = [BC.DECIMALLONGITUDE, BC.DECIMALLATITUDE],
    ) -> None:
        cols = [x.value for x in cols]
        df = pd.read_csv(data_path, sep="\t")
        self.df = df[cols]

    def get_row(self) -> pd.Series:
        raise NotImplementedError


if __name__ == "__main__":
    bd = BirdDataset(data_processed_path() / "1000/LBBG_ZEEBRUGGE.txt")
    print(bd.df)
