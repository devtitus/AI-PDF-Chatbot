from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def create_vector_store(chunks):
    """
    Takes document chunks, generates HuggingFace embeddings, and creates a FAISS vector store.
    """
    # Use a lightweight HF model by default
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store
