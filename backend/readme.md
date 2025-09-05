# Chatbot Backend

This project provides a backend pipeline for document loading, chunking, embedding, and vector storage using ChromaDB.

## Folder Structure

```
chatbot/
  backend/
    .env                # Environment variables (e.g., API keys)
    chunks.py           # Splits documents into smaller chunks for embedding
    embeder.py          # Embeds text chunks using HuggingFace models
    loader.py           # Loads documents from various file formats
    main.py             # Main script to run the pipeline
    sample.txt          # Example text file with Q&A pairs
    store.py            # Stores vectors in ChromaDB
    __pycache__/        # Python cache files
    data/
      Fastapi.pdf       # Example PDF file for testing
```

## File Descriptions

- **.env**: Stores sensitive environment variables such as API keys.
- **chunks.py**: Contains [`chunk_documents`](backend/chunks.py) for splitting documents into manageable chunks.
- **embeder.py**: Contains [`embed_chunks`](backend/embeder.py) for generating embeddings from text chunks.
- **loader.py**: Contains [`load_all_files`](backend/loader.py) for loading documents from the `data/` directory.
- **main.py**: Example script that loads, chunks, embeds, and prints vectors.
- **sample.txt**: Sample text data for testing loaders.
- **store.py**: Contains [`save_vectors_to_chroma`](backend/store.py) for saving embeddings to ChromaDB.
- **data/**: Directory for storing input files (e.g., PDFs).
- **__pycache__/**: Auto-generated Python bytecode cache.

## Usage

1. Place your documents in the `data/` folder.
2. Run `main.py` to process the documents and generate embeddings.
3. Use `store.py` to save embeddings to ChromaDB.

---

**Note:** Make sure to install all required dependencies (see code for package requirements).