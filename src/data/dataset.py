from pathlib import Path
import pandas as pd
import numpy as np
from src.data.birdcols import BirdColumns as BC
from src import data_processed_path
from abc import ABC, abstractmethod


class BaseDataset(ABC):
    @abstractmethod
    def get_data(self) -> np.ndarray:
        pass


class BirdDataset(BaseDataset):
    def __init__(
        self,
        data_path: Path,
        cols: list[BC] = [BC.DECIMALLONGITUDE, BC.DECIMALLATITUDE],
    ) -> None:
        cols = [x.value for x in cols]
        df = pd.read_csv(data_path, sep="\t")

        self.cols = cols
        self.df: pd.DataFrame = df[cols]

    def standardise(self) -> None:
        raise NotImplementedError

    def normalise(self) -> None:
        raise NotImplementedError

    def get_data(self) -> np.ndarray:
        return self.df.to_numpy()


if __name__ == "__main__":
    bd = BirdDataset(data_processed_path() / "1000/LBBG_ZEEBRUGGE.txt")
    print(bd.df)
