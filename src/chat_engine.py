from langchain_community.llms import Ollama
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def get_chat_chain(vector_store, model_name="gemma3:1b"):
    """
    Initializes the RAG chain with Ollama and the FAISS vector store.
    """
    llm = Ollama(model=model_name)
    
    # Use vector store as retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    system_prompt = (
        "You are an AI assistant tasked with answering questions based on the provided document context. "
        "If you don't know the answer based on the context, just say that you don't know, don't try to make up an answer. "
        "Context: {context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
    
    return retrieval_chain
