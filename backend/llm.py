from openai import OpenAI
from retrival import retrieve_from_chroma
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Get the API key
api_key = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


def generate_answer(question: str, persist_dir="chroma_db", top_k=3):
    """Generate an answer using retrieved context + OpenRouter LLM."""
    results = retrieve_from_chroma(question, persist_dir, top_k)

    # Build context string from retrieved docs
    contexts = []
    for meta in results["metadatas"][0]:
        ctx = " ".join([f"{k}: {v}" for k, v in meta.items()])
        contexts.append(ctx)
    context_text = "\n".join(contexts)

    prompt = f"""
You are a helpful assistant. Use the following retrieved context to answer the question.

Context:
{context_text}

Question: {question}

Answer:
"""
    
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",  # You can use gpt-4, llama, etc.
        messages=[
            {"role": "system", "content": "You are a knowledgeable assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content
