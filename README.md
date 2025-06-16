# 🔍 LLM Power Search: Open Source License Navigator (Offline RAG with Mistral + llama.cpp)

> 🧠 A fast, local RetrievalQA pipeline that runs entirely on your Mac (M1/M2) — no paid APIs, no cloud calls.

---

## 🚀 What This Project Does

This repo showcases an **end-to-end RAG system** that answers real-world legal questions about open source software licenses — **entirely offline** using the Mistral-7B model in GGUF format.

**Key features:**
- 🧠 Local LLM inference using `llama.cpp`
- 🔎 Semantic search using `FAISS` + sentence-transformers
- 📄 License documents indexed and queried via LangChain’s `RetrievalQA`
- ⚙️ Model benchmarking with variable GPU layer offloading

---
## 🧪 Sample Questions Answered by the System

- Q1: Can the OSC License be used for commercial products?
- Q2: Does the MIT License require attribution in binary distributions?
- Q3: Does the Apache 2.0 license require modified files to be marked as changed?
- Q4: Does the ISC License mention data privacy obligations?
- Q5: Is there any liability clause in the Zero-Clause BSD license?
- Q6: If I use code under the Academic Free License, do I need to include a patent grant?

---

## 📊 Benchmark: Inference Speed vs GPU Layer Count

| GPU Layers | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 |
| ---------- | --- | --- | --- | --- | --- | --- |
| 0 | 36.86 | 18.07 | 11.59 | 19.83 | 58.67 | 32.08 |
| 6 | 34.49 | 16.77 | 10.76 | 19.25 | 48.54 | 32.55 |
| 13 | 30.56 | 15.07 | 10.22 | 16.22 | 39.84 | 26.40 |
| 19 | 28.03 | 13.08 | 9.33 | 13.87 | 40.24 | 22.41 |
| 28 | 20.31 | 8.92 | 7.14 | 9.75 | 30.28 | 14.12 |
| 37 | 15.29 | 7.48 | 6.35 | 8.26 | 19.48 | 11.03 |
| 46 | 15.10 | 6.97 | 6.15 | 7.78 | 19.79 | 10.98 |
| 55 | 15.06 | 6.88 | 5.53 | 7.62 | 18.97 | 11.10 |
| 64 | 15.82 | 7.01 | 5.68 | 7.87 | 19.69 | 10.96 |

<img width="893" alt="QGraph" src="https://github.com/user-attachments/assets/3186c0ae-9648-4593-bd64-5d1a79050327" />

#### NOTE
> 🔗 [See full terminal outputs →](https://github.com/santhoshnumberone/LLM-Power-Search-for-Open-Source-Licensing-Navigator/blob/main/terminalOuput.md)



---

## 💻 Local Setup (Mac M1/M2, Offline)

```
# System setup
brew install cmake
CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python
```
# Python packages
`pip install langchain faiss-cpu langchain-huggingface sentence-transformers langchain-community tqdm`

# 🔽 Download Mistral model:

`wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q3_K_M.gguf`
Change the path in `step5_llm_loader.py` line 5 to path where you downloaded the `Mistral model` 

# 📂 Project Files
| Step | File                           | Description                    |
| ---- | ------------------------------ | ------------------------------ |
| ✅ 1  | `step1_generate_index.py`      | Loads raw license data         |
| ✅ 2  | `step2_generate_embeddings.py` | Converts docs into embeddings  |
| ✅ 3  | `step3_build_faiss_index.py`   | FAISS vector index             |
| ✅ 4  | `step4_load_faiss_index.py`   | load FAISS vector index        |
| ✅ 5  | `step5_llm_loader.py`          | Loads Mistral via `llama.cpp`  |
| ✅ 6  | `step6_retrieval_qa.py`        | RAG pipeline via `RetrievalQA` |

▶️ Run Instructions
```
python step1_generate_index.py
python step2_generate_embeddings.py
python step3_build_faiss_index.py
python step4_load_faiss_index.py
python step5_llm_loader.py
python step6_retrieval_qa.py
```

Edit GPU layer offload in: 

[step5_llm_loader.py](https://github.com/santhoshnumberone/LLM-Power-Search-for-Open-Source-Licensing-Navigator/blob/main/step5_llm_loader.py) → n_gpu_layers = X (line 11)

## 🛡 License

This project is open-source under the MIT License. See the [LICENSE](./LICENSE) file for details.

### 👤 About the Creator

I'm an AI Product Builder and Prompt Engineer-in-transition, focused on building real-world tools that can run efficiently on edge devices. This repo is part of a portfolio designed to showcase:

 - Efficient use of local LLMs
 - Product thinking for real legal use cases
 - Optimization and benchmarking for real-world speed

## 📬 Let's Connect
If you’re hiring for a role that demands prototyping LLM tools, evaluating AI stack tradeoffs, or shaping the UX of intelligent systems, let’s talk.

[📫 LinkedIn →](www.linkedin.com/in/santhosh-electraanu)
