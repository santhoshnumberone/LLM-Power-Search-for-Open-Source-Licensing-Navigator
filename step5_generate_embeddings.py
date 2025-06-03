
from tqdm import tqdm
from langchain_huggingface import HuggingFaceEmbeddings
import json
import os
from pathlib import Path

# Paths

chunks_dir = Path(__file__).parent / "intermediate/chunks"
embeddings_dir = Path(__file__).parent / "intermediate/embeddings"



# Paths
# chunks_dir = Path("intermediate/chunks")
# embeddings_dir = Path("intermediate/embeddings")
embeddings_dir.mkdir(parents=True, exist_ok=True)

# Initialize embedding model
embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Process each chunk file
for chunk_file in tqdm(sorted(chunks_dir.glob("*.txt")), desc="🔍 Generating Embeddings"):
    license_id = chunk_file.stem
    with open(chunk_file, "r") as f:
        chunks = f.read().split("\n\n")

    # Skip if no valid chunks
    if not any(chunks):
        print(f"⚠️ Skipping {license_id}: no content")
        continue

    vectors = embedder.embed_documents(chunks)
    
    # Save as JSON
    output_path = embeddings_dir / f"{license_id}.json"
    with open(output_path, "w") as f:
        json.dump({
            "license_id": license_id,
            "chunks": chunks,
            "vectors": vectors
        }, f)

print(f"\n✅ Embeddings saved to {embeddings_dir}")
