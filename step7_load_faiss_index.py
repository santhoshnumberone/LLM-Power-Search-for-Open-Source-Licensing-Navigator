import faiss
import json
from pathlib import Path


def load_faiss_index(
    index_path=str(Path(__file__).parent / "faiss_index/full_text.index"),
    metadata_path=str(Path(__file__).parent / "faiss_index/full_text_metadata.json")
):
    index_file = Path(index_path)
    metadata_file = Path(metadata_path)

    if not index_file.exists() or not metadata_file.exists():
        raise FileNotFoundError("FAISS index or metadata not found. Run `build_faiss_index.py` first.")

    # Load FAISS index
    index = faiss.read_index(str(index_file))

    # Load metadata
    with open(metadata_file) as f:
        metadata = json.load(f)

    print(f"✅ FAISS index reloaded with {len(metadata)} entries")
    return index, metadata


# For standalone testing
if __name__ == "__main__":
    index, metadata = load_faiss_index()
