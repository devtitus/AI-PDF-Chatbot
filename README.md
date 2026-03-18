# AI PDF Chatbot 📄

A privacy-first, fully local AI PDF Chatbot that allows you to upload PDF documents and ask questions about their content. Built with **LangChain**, **FAISS**, **HuggingFace**, and **Ollama**, this application ensures your data never leaves your machine.

## Features
- **Local Parsing**: Uses `PyPDFLoader` to securely parse documents locally.
- **Efficient Retrieval**: Chunks text and caches it in a highly performant **FAISS** vector database.
- **High-Quality Embeddings**: Utilizes HuggingFace's `all-MiniLM-L6-v2` for generating precise embeddings.
- **Privacy-First LLM**: Answers questions using local LLMs (like `gemma3:1b`, `llama3`, `mistral`) served via **Ollama**.
- **Interactive UI**: A sleek, minimal web interface built with **Streamlit**.

## Running the Application

### Prerequisites
1. **Python 3.9+**
2. **Ollama**: Download and install [Ollama](https://ollama.com/)
3. Pull your preferred local model. For example: `ollama pull gemma3:1b` or `ollama pull llama3`

### Installation
1. Clone the repository and navigate to the project directory.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   
   # Windows
   .\venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Start the Streamlit development server:
```bash
streamlit run app.py
```
1. The web UI will automatically open in your browser (`http://localhost:8501`).
2. Select your Ollama model from the sidebar.
3. Upload your PDF, click **Process PDF**, and start chatting!
