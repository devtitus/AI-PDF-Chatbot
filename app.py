import streamlit as st
from src.document_processor import process_pdf
from src.vector_store import create_vector_store
from src.chat_engine import get_chat_chain

st.set_page_config(page_title="AI PDF Chatbot", page_icon="📄", layout="centered")

st.title("📄 AI PDF Chatbot")
st.markdown("Upload a PDF document and ask questions about its content powered by LangChain and Ollama.")

# Initialize session state variables
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "retrieval_chain" not in st.session_state:
    st.session_state.retrieval_chain = None

# Sidebar for controls and upload
with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    ollama_model = st.selectbox("Select Ollama Model", ["gemma3:1b", "mistral", "llama3.2", "phi3"], index=0)
    
    if st.button("Process PDF"):
        if uploaded_file is not None:
            with st.spinner("Processing PDF..."):
                try:
                    file_bytes = uploaded_file.read()
                    chunks = process_pdf(file_bytes, uploaded_file.name)
                    
                    if chunks:
                        st.session_state.vector_store = create_vector_store(chunks)
                        st.session_state.retrieval_chain = get_chat_chain(st.session_state.vector_store, model_name=ollama_model)
                        st.success("PDF processed successfully! You can now ask questions.")
                    else:
                        st.error("Failed to process the PDF or it was empty.")
                except Exception as e:
                    st.error(f"Error processing PDF: {e}")
        else:
            st.warning("Please upload a PDF file first.")

# Main Chat Interface
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about the document..."):
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        if st.session_state.retrieval_chain is None:
            st.warning("Please upload and process a PDF document first.")
        else:
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.retrieval_chain.invoke({"input": prompt})
                    answer = response.get("answer", "No answer generated.")
                    st.markdown(answer)
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})
                    
                    with st.expander("Show source chunks"):
                        for i, doc in enumerate(response.get("context", [])):
                            st.markdown(f"**Chunk {i+1}:**")
                            st.text(doc.page_content[:500] + "...")
                except Exception as e:
                    st.error(f"Error generating answer: {e}")
