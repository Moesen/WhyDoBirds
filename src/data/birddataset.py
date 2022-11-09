from pathlib import Path
import pandas as pd
from src.data.birdcols import BirdColumns as BC

class BirdDataset:
    def __init__(
        self,
        data_path: Path,
        cols: list[BC] = [BC.DECIMALLONGITUDE, BC.DECIMALLATITUDE],
    ) -> None:
        df = pd.read_csv(data_path, sep="\t")
        self.df = df[cols]
