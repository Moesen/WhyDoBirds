from abc import ABC, abstractmethod
from pygel3d.graph import Graph
import numpy as np

class BaseGraph(ABC):
    @abstractmethod
    def __init__(self, g_array: np.ndarray) -> None:
        pass
    
    @abstractmethod
    def create_pygel_graph(self, g_array: np.ndarray) -> Graph:
        pass

class SimpleGraph(BaseGraph):
    pass
