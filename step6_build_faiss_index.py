import faiss
import numpy as np
import json
from pathlib import Path

# Directories
embedding_dir = Path(__file__).parent / "intermediate/embeddings"
index_dir = Path(__file__).parent / "faiss_index"
index_dir.mkdir(parents=True, exist_ok=True)

# Output paths
index_path = index_dir / "full_text.index"
metadata_path = index_dir / "full_text_metadata.json"

all_vectors = []
metadata = []

# Load embeddings and collect vectors + metadata
for json_file in sorted(embedding_dir.glob("*.json")):
    with open(json_file, "r") as f:
        data = json.load(f)

    license_id = data["license_id"]
    chunks = data["chunks"]
    vectors = data["vectors"]

    for i, vec in enumerate(vectors):
        all_vectors.append(vec)
        metadata.append({
            "license_id": license_id,
            "chunk_index": i,
            "text": chunks[i]
        })

# Create and populate FAISS index
dim = len(all_vectors[0])
index = faiss.IndexFlatL2(dim)
index.add(np.array(all_vectors).astype("float32"))

# Save index and metadata
faiss.write_index(index, str(index_path))
with open(metadata_path, "w") as f:
    json.dump(metadata, f, indent=2)

print(f"✅ FAISS index written to {index_path}")
print(f"✅ Metadata written to {metadata_path}")
