from pathlib import Path

def root_path() -> Path:
    return Path(__file__).parent.parent

def data_raw_path() -> Path:
    return root_path() / "data/raw"

def data_processed_path() -> Path:
    return root_path() / "data/processed"

if __name__ == "__main__":
    print(root_path())
    print(data_raw_path())
    print(data_processed_path())
