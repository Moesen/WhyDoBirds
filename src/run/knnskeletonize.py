from src.data.dataset import BirdDataset
from src.skeletonize import skeletonize, clustering
from src import data_processed_path
from pygel3d import hmesh, gl_display as gl

if __name__ == "__main__":
    bd = BirdDataset(data_processed_path() / "1000/LBBG_ZEEBRUGGE.txt")
    cluster = clustering.KnnClustering.create_graph(bd)
    
