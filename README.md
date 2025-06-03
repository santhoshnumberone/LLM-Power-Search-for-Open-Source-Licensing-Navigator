# LLM-Power-Search-for-Open-Source-Licensing-Navigator
# 🔍 LLM Open Source License RAG (Local Mistral + llama.cpp)

> A blazing-fast, offline RetrievalQA system that runs entirely on your MacBook (M1/M2) without APIs.

## 🚀 Overview

This repo contains a complete Retrieval-Augmented Generation pipeline built using:
- Mistral-7B-Instruct in GGUF Q3_K_M format
- llama-cpp
- FAISS vector search
- LangChain’s RetrievalQA chain
- Benchmarking scripts for GPU layer speed comparison

## 🔍 Sample Questions
- Q1: Can the OSC License be used for commercial products?				
- Q2: Does the MIT License require attribution in binary distributions?			
- Q3: Does the Apache 2.0 license require modified files to be marked as changed?
- Q4: Does the ISC License mention data privacy obligations?
- Q5: Is there any liability clause in the Zero-Clause BSD license?
- Q6: If I use code under the Academic Free License, do I need to include a patent grant?


## 📊 Benchmark: Inference Time(sec) vs GPU Layers
|     | Layers 0 | Layers 6 | Layers 13 | Layers 19 | Layers 28 | Layers 37 | Layers 46 | Layers 55 | Layers 64 |
| --- | -------- | -------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| Q1  | 36.86    | 34.49    | 30.56     | 28.03     | 20.31     | 15.29     | 15.1      | 15.06     | 15.82     |
| Q2  | 18.07    | 16.77    | 15.07     | 13.08     | 8.92      | 7.48      | 6.97      | 6.88      | 7.01      |
| Q3  | 11.59    | 10.76    | 10.22     | 9.33      | 7.14      | 6.35      | 6.15      | 5.53      | 5.68      |
| Q4  | 19.83    | 19.25    | 16.22     | 13.87     | 9.75      | 8.26      | 7.78      | 7.62      | 7.87      |
| Q5  | 58.67    | 48.54    | 39.84     | 40.24     | 30.28     | 19.48     | 19.79     | 18.97     | 19.69     |
| Q6  | 32.08    | 32.55    | 26.4      | 22.41     | 14.12     | 11.03     | 10.98     | 11.1      | 10.96     |

<img width="893" alt="QGraph" src="https://github.com/user-attachments/assets/3186c0ae-9648-4593-bd64-5d1a79050327" />


## 📂 Project Structure

- `step1_generate_index.py` — loads license data
- `step2_generate_embeddings.py` — sentence-transformers
- `step3_build_faiss_index.py` — FAISS vector index
- `step4_llm_loader.py` — Load Mistral via llama.cpp
- `step5_retrieval_qa.py` — RetrievalQA chain

## 🛠️ Setup (Mac M1/M2)

```
brew install cmake
CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python
pip install langchain faiss-cpu
pip install -U langchain-huggingface
pip install sentence-
pip install langchain-community
pip install tqdm
```
## Download Mistral model:

`wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q3_K_M.gguf`

## 💡 How to Run
`python step1_generate_index.py`

`python step2_generate_embeddings.py`

`python step3_build_faiss_index.py.py`

`python step4_llm_loader.py`

`python step5_retrieval_qa.py`

