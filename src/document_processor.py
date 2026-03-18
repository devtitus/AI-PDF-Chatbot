from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tempfile
import os

def process_pdf(uploaded_file_bytes, filename):
    """
    Saves uploaded file byte data to a temporary file, loads it, and splits into chunks.
    """
    # Create a temporary file
    temp_dir = tempfile.mkdtemp()
    temp_path = os.path.join(temp_dir, filename)
    
    with open(temp_path, "wb") as f:
        f.write(uploaded_file_bytes)
    
    try:
        # Load using PyPDFLoader
        loader = PyPDFLoader(temp_path)
        documents = loader.load()
        
        # Split the documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_documents(documents)
        return chunks
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)
