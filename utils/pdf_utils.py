import streamlit as st
import os

# Try to import optional dependencies
try:
    from PyPDF2 import PdfReader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_google_genai import GoogleGenerativeAIEmbeddings
    from langchain_community.vectorstores import FAISS
    from langchain.chains.question_answering import load_qa_chain
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.prompts import PromptTemplate
    PDF_DEPENDENCIES_LOADED = True
except ImportError:
    # Silently set flag without showing warning
    PDF_DEPENDENCIES_LOADED = False

def get_pdf_text(pdf_docs):
    """
    Extract text from uploaded PDF documents.
    
    Args:
        pdf_docs: List of uploaded PDF files
        
    Returns:
        str: Extracted text from all PDF documents
    """
    if not PDF_DEPENDENCIES_LOADED:
        # Silently return empty string without showing error
        return ""
        
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
        except Exception as e:
            # Silently continue without showing error
            pass
    return text

def get_text_chunks(text):
    """
    Split text into manageable chunks for embedding.
    
    Args:
        text: Text to split
        
    Returns:
        list: List of text chunks
    """
    if not PDF_DEPENDENCIES_LOADED:
        # Silently return empty list without showing error
        return []
        
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        return chunks
    except Exception as e:
        # Silently return empty list without showing error
        return []

def get_vector_store(text_chunks):
    """
    Create a vector store from text chunks using Google Generative AI embeddings.
    
    Args:
        text_chunks: List of text chunks to embed
        
    Returns:
        FAISS: Vector store with embedded chunks
    """
    if not PDF_DEPENDENCIES_LOADED:
        # Show more detailed error info
        st.error("Required PDF dependencies are not loaded.")
        return None
        
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("Google API key is missing. Please set the GOOGLE_API_KEY environment variable.")
            return None
            
        if not text_chunks or len(text_chunks) == 0:
            st.error("No text chunks to process. Please ensure the PDF contains extractable text.")
            return None
            
        # Debug info
        st.info(f"Creating embeddings for {len(text_chunks)} text chunks with API key: {api_key[:4]}...")
        
        # Use the correct model name format for Google Generative AI embeddings
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",  # Correct format with models/ prefix
            google_api_key=api_key
        )
        vector_store = FAISS.from_texts(text_chunks, embeddings)
        return vector_store
    except Exception as e:
        st.error(f"Error creating vector store: {str(e)}")
        return None

def get_conversational_chain():
    """
    Create a conversational chain using Google Generative AI.
    
    Returns:
        chain: QA chain for answering questions
    """
    if not PDF_DEPENDENCIES_LOADED:
        st.error("Required PDF dependencies are not loaded.")
        return None
        
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("Google API key is missing. Please set the GOOGLE_API_KEY environment variable.")
            return None
            
        prompt_template = """
        You are a dermatologist AI assistant. Use the context provided to answer the user's question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Always maintain a professional and medical tone. Include relevant medical details when available.
        
        Context: {context}
        
        Question: {question}
        
        Answer:
        """
        
        # Debug info
        st.info(f"Creating conversation chain with Gemini model using API key: {api_key[:4]}...")
        
        # Use the correct model name format for Google Generative AI
        model = ChatGoogleGenerativeAI(
            model="gemini-pro",  # Use gemini-pro without models/ prefix
            google_api_key=api_key,
            temperature=0.3
        )
        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
        return chain
    except Exception as e:
        st.error(f"Error creating conversation chain: {str(e)}")
        return None

def process_question(user_question, vector_store, chain):
    """
    Process a user question using the vector store and conversational chain.
    
    Args:
        user_question: User's query
        vector_store: FAISS vector store with embedded text
        chain: QA chain for answering questions
        
    Returns:
        str: AI's response
    """
    if not PDF_DEPENDENCIES_LOADED:
        st.error("Required PDF dependencies are not loaded.")
        return "I need to process your PDF documents first. Please upload and process your documents, then try asking again."
        
    try:
        if not vector_store or not chain:
            st.warning("Vector store or conversation chain is not initialized.")
            return "I need to process your PDF documents first. Please upload and process your documents, then try asking again."
        
        # Debug info
        st.info(f"Searching for relevant content about: '{user_question}'")
        
        docs = vector_store.similarity_search(user_question)
        
        if not docs or len(docs) == 0:
            st.warning("No relevant documents found for your question.")
            return "I couldn't find any relevant information in the uploaded documents to answer your question. Please try a different question or upload more relevant documents."
        
        # Debug info
        st.info(f"Found {len(docs)} relevant document chunks. Generating response...")
        
        # Use the invoke method instead of run
        response = chain.invoke({"input_documents": docs, "question": user_question})
        
        # Debug info about response type
        st.info(f"Response type: {type(response)}")
        
        # Extract the content from the response
        if isinstance(response, dict) and "answer" in response:
            return response["answer"]
        elif isinstance(response, dict) and "output_text" in response:
            return response["output_text"]
        elif isinstance(response, str):
            return response
        else:
            # Show the raw response for debugging
            st.code(str(response))
            return str(response)
    except Exception as e:
        st.error(f"Error processing question: {str(e)}")
        return f"I'm having trouble processing your question right now: {str(e)}. Please try again or upload a different document."
