from step8_llm_loader import load_llm
from step7_load_faiss_index import load_faiss_index
from sentence_transformers import SentenceTransformer
import numpy as np
import time

# Load LLM and FAISS index once (warm start)
llm = load_llm()
index, metadata = load_faiss_index()
embedder = SentenceTransformer("all-MiniLM-L6-v2")
TOP_K = 2

# Prompt format
def format_prompt(question, chunks):
    context = "\n---\n".join(chunks)
    return f"""
Answer the question in a single crisp sentence using the context below. If unsure, say you don't know.

Context:
{context}

Question: {question}
Answer:
""".strip()

# RetrievalQA
def query_licensing_navigator(user_question):
    start_time = time.time()

    # Step 1: Embed question
    question_embedding = embedder.encode([user_question])

    # Step 2: FAISS vector search
    scores, indices = index.search(np.array(question_embedding).astype("float32"), TOP_K)

    # Step 3: Retrieve corresponding chunks
    retrieved_chunks = [metadata[i]["text"] for i in indices[0] if i < len(metadata)]

    # Logging block start
    print("=" * 60)
    print(f"❓ Q: {user_question}")

    if not retrieved_chunks:
        print("⚠️ No relevant chunks retrieved from FAISS index.")
        print("⏱️ Latency: {:.2f} seconds".format(time.time() - start_time))
        print("❌ Answer: Not enough context to answer this question.\n")
        return "No answer – no context retrieved."

    # Step 4: Format prompt
    prompt = format_prompt(user_question, retrieved_chunks)

    # Step 5: LLM response
    response = llm(prompt, max_tokens=128, stop=["\n"])
    answer = response["choices"][0]["text"].strip()

    elapsed = time.time() - start_time

    # ✅ Logging
    print(f"📥 Retrieved Chunks:\n{retrieved_chunks[0]}\n...\n{retrieved_chunks[-1]}")
    print(f"🧠 Prompt tokens: ~{len(prompt.split())}")
    print(f"⏱️ Latency: {elapsed:.2f} seconds")
    print(f"✅ Answer: {answer}")
    print("=" * 60)

    return answer

# Evaluation batch
if __name__ == "__main__":
    
    eval_questions = [
        # 1. Retrieval + clarity check
        "Can the OSC License be used for commercial products?",

        # 2. One-liner factual precision + chunk relevance
        "Does the MIT License require attribution in binary distributions?",

        # 3. Prompt compression test (medium-length legal clause)
        "Does the Apache 2.0 license require modified files to be marked as changed?",

        # 4. Unclear/unavailable info test (to test 'Flag unclear answers')
        "Does the ISC License mention data privacy obligations?",

        # 5. Edge case retrieval + token size logging
        "Is there any liability clause in the Zero-Clause BSD license?",

        # 6. Instruction-following style with subtle phrasing (indirect query)
        "If I use code under the Academic Free License, do I need to include a patent grant?"
    ]

    print("🚀 Starting batch evaluation of 6 licensing queries...\n")
    for q in eval_questions:
        query_licensing_navigator(q)
