import os
from pathlib import Path
from typing import List
from langchain_core.documents import Document

# ✅ All loaders come from langchain_community
from langchain_community.document_loaders import (
    PyMuPDFLoader,                  # PDF
    UnstructuredExcelLoader,        # Excel
    UnstructuredHTMLLoader,         # HTML
    TextLoader,                     # TXT
    UnstructuredWordDocumentLoader, # DOCX
)


def load_all_files(data_folder: str = "data") -> List[Document]:
    """
    Load all supported files from the given folder using langchain_community.
    Returns a list of Document objects.
    """
    docs: List[Document] = []
    folder_path = Path(data_folder).resolve()

    if not folder_path.exists():
        raise FileNotFoundError(f"❌ Folder not found: {folder_path}")

    for file in folder_path.iterdir():
        if not file.is_file():
            continue

        ext = file.suffix.lower()
        loader = None

        try:
            if ext == ".pdf":
                loader = PyMuPDFLoader(str(file))
            elif ext in [".xls", ".xlsx"]:
                loader = UnstructuredExcelLoader(str(file))
            elif ext in [".html", ".htm"]:
                loader = UnstructuredHTMLLoader(str(file))
            elif ext == ".txt":
                loader = TextLoader(str(file), encoding="utf-8")
            elif ext == ".docx":
                loader = UnstructuredWordDocumentLoader(str(file))
            else:
                print(f"[SKIP] Unsupported file type: {file.name}")
                continue

            loaded_docs = loader.load()

            # Add source metadata
            for d in loaded_docs:
                d.metadata["source"] = file.name

            docs.extend(loaded_docs)
            print(f"[OK] Loaded {file.name}")

        except Exception as e:
            print(f"[ERR] Failed to load {file.name}: {e}")

    return docs
