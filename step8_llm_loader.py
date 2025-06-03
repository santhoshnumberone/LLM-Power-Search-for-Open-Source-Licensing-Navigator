from llama_cpp import Llama
from pathlib import Path

# Use Q3_K_M for lower RAM usage (you mentioned switching to it)
model_path = (Path(__file__).parent.parent / "shared/models/mistral-7b-instruct-v0.1.Q3_K_M.gguf").resolve()

def load_llm(
    model_path=str(model_path),
    n_ctx=512,         # Small context for RAM constraint
    n_batch=16,        # Reduce if you hit OOM
    gpu_layers=0       # 0 = CPU only for 8GB Mac
):
    print(f"🔄 Loading Mistral model from: {model_path}")
    llm = Llama(
        model_path=model_path,
        n_ctx=n_ctx,
        n_batch=n_batch,
        n_threads=4,        # Match your CPU cores
        n_gpu_layers=gpu_layers,
        use_mlock=True,     # Lock memory to avoid swap
        verbose=False
    )
    print("✅ Mistral LLM loaded successfully")
    return llm

# For standalone test
if __name__ == "__main__":
    load_llm()
