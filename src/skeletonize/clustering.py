from abc import ABC, abstractmethod
from src.data.dataset import BaseDataset
from src.skeletonize.graph import BaseGraph
import numpy as np
import scipy.spatial
from tqdm import tqdm


class BaseAggregation(ABC):
    @abstractmethod
    def create_graph(cls, dataset: BaseDataset) -> BaseGraph:
        pass


class KnnClustering(BaseAggregation):
    @classmethod
    def create_graph(cls, dataset: BaseDataset, k: int = 3) -> BaseGraph:
        arr: np.ndarray = dataset.get_data()
        tree = scipy.spatial.KDTree(arr)
        size: int = arr.shape[0]
        g = np.zeros((size, size), dtype=np.float32)

        for i, row in tqdm(enumerate(arr), total=size):
            pos, indices = tree.query(row, k=k)
            closest_indices = indices[indices != i] # type:ignore

            g[i, closest_indices] = 1
            g[closest_indices, i] = 1

        return BaseGraph(g)
