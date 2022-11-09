from abc import ABC, abstractmethod
from src.data.dataset import AbstractDataset


class AbstractBirdAggregation(ABC):
    @abstractmethod
    def aggregate(self, dataset: AbstractDataset) -> None:
        pass


