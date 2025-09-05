from loader import load_all_files
from chunks import chunk_documents
from embeder import embed_chunks
from store import save_vectors_to_chroma
from retrival import retrieve_from_chroma
from llm import generate_answer


doc = load_all_files("data")
chunks_doc = chunk_documents(doc)
vectors = embed_chunks(chunks_doc)
collection = save_vectors_to_chroma(vectors)

user_question = input("Enter your prompt: ")

results = retrieve_from_chroma(user_question)

response = generate_answer(user_question)
print(response)



# print(print)