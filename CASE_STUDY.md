# Title
AI PDF Chatbot: A Local, Privacy-First RAG Application

# Tagline
Chat with your documents securely using state-of-the-art local LLMs and vector search.

# slug
ai-pdf-chatbot-secure-local-rag

# Short description in 2 sentence
Built a fully local Retrieval-Augmented Generation (RAG) application that allows users to seamlessly upload and query PDF documents without compromising privacy. The system utilizes LangChain for orchestration, FAISS for instantaneous vector search, and Ollama to generate context-aware LLM answers entirely offline.

# Tags
Artificial Intelligence, RAG, LLM, Python, LangChain, Privacy, Machine Learning, Streamlit

# Technologies
- Python
- LangChain / LangChain Classic
- Streamlit
- FAISS (Facebook AI Similarity Search)
- HuggingFace Embeddings (all-MiniLM-L6-v2)
- Ollama (gemma3:1b, llama3, mistral)
- PyPDF

# A Detailed markdown about the project with all the details

## The Problem
With the rapid adoption of AI, businesses and individuals face a critical challenge: how to leverage the power of Large Language Models (LLMs) on sensitive or proprietary documents without exposing data to third-party APIs. Cloud-based solutions often pose unacceptable privacy risks, cost barriers, and latency issues, restricting users from interacting with highly confidential files like financial reports, medical records, or legal contracts.

## The Solution
To address this, I developed the **AI PDF Chatbot**, a fully local Retrieval-Augmented Generation (RAG) pipeline. This application guarantees that not a single byte of document data leaves the host machine. 

Users can upload any PDF via an intuitive, minimalist UI. The backend immediately processes the document, intelligently chunks the text to preserve context, creates numerical representations (embeddings) of the text, and stores them in a lightning-fast vector database. When a user asks a question, the application retrieves the most semantically relevant text chunks and seamlessly hands them off to an open-source local LLM, which formulates an accurate, context-aware answer.

## System Architecture

1. **Document Ingestion & Chunking**: 
   - Used LangChain's `PyPDFLoader` to parse complex PDF layouts.
   - Implemented `RecursiveCharacterTextSplitter` to divide the document into manageable 1000-character chunks with a 200-character overlap, ensuring that sentences, paragraphs, and critical context are never prematurely cut off.
2. **Embeddings & Vector Search**: 
   - Integrated HuggingFace's `all-MiniLM-L6-v2` embedding model—a lightweight but incredibly accurate model tailored for semantic search on local hardware.
   - Built an in-memory FAISS (Facebook AI Similarity Search) vector store, which indexes these embeddings and enables sub-millisecond retrieval of relevant context.
3. **Local LLM Integration**: 
   - Utilized Ollama to serve modern open-source language models locally (such as `gemma3:1b`, `llama3`, and `mistral`).
   - Integrated the `create_retrieval_chain` protocol from LangChain Classic to act as the cognitive bridge, injecting the retrieved FAISS contexts directly into the LLM context window to prevent generative hallucinations.
4. **User Interface**: 
   - Built a sleek, responsive frontend using Streamlit, allowing users to select their desired local model, upload files, and maintain an ongoing conversational chat history.

## Results & Impact
The final application successfully democratizes RAG technology. It operates entirely offline, enabling researchers, professionals, and privacy-conscious users to instantly "talk" to dense, multi-page PDFs with zero risk of data leakage. Furthermore, by keeping the models local, the application completely bypasses API waiting times and rate limits, creating a fast, fluid, and completely free user experience.
