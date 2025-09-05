# embedder.py
from typing import List
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

def embed_chunks(chunks: List[Document]):
    """
    Embed text chunks using Hugging Face embeddings (BAAI/bge-large-en-v1.5).
    """
    model_name = "BAAI/bge-large-en-v1.5"

    embedding_model = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": "cpu"},       # change to "cuda" for GPU
        encode_kwargs={"normalize_embeddings": True}
    )

    vectors = embedding_model.embed_documents(
        [chunk.page_content for chunk in chunks]
    )
    return vectors
