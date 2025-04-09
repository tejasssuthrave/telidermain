import os
import streamlit as st
import tempfile
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# Flag to check if dependencies are loaded
PDF_DEPENDENCIES_LOADED = True

try:
    # Check if required packages are available
    from PyPDF2 import PdfReader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    from langchain_community.vectorstores import FAISS
    from langchain.chains.question_answering import load_qa_chain
    from langchain.prompts import PromptTemplate
except ImportError:
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
        st.error("Required PDF dependencies are not loaded.")
        return ""
        
    text = ""
    try:
        for pdf in pdf_docs:
            # Create a temporary file to save the uploaded PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(pdf.read())
                tmp_file_path = tmp_file.name
                
            # Read the PDF file
            pdf_reader = PdfReader(tmp_file_path)
            
            # Extract text from each page
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:  # Check if text was extracted
                    text += page_text
                    
            # Clean up the temporary file
            os.unlink(tmp_file_path)
            
        if not text.strip():
            st.warning(f"No text could be extracted from {pdf.name}. The PDF may be scanned or contain only images.")
            
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return ""

def get_text_chunks(text):
    """
    Split text into manageable chunks for embedding.
    
    Args:
        text: Text to split
        
    Returns:
        list: List of text chunks
    """
    if not PDF_DEPENDENCIES_LOADED:
        st.error("Required PDF dependencies are not loaded.")
        return []
        
    try:
        # Create a text splitter with specified parameters
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        
        # Split the text into chunks
        chunks = text_splitter.split_text(text)
        
        # Log the number of chunks created
        st.info(f"Created {len(chunks)} text chunks for processing")
        
        return chunks
    except Exception as e:
        st.error(f"Error splitting text into chunks: {str(e)}")
        return []

def get_vector_store(text_chunks):
    """
    Create a vector store from text chunks using OpenAI embeddings.
    
    Args:
        text_chunks: List of text chunks to embed
        
    Returns:
        FAISS: Vector store with embedded chunks
    """
    if not PDF_DEPENDENCIES_LOADED:
        st.error("Required PDF dependencies are not loaded.")
        return None
        
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("OpenAI API key is missing. Please set the OPENAI_API_KEY environment variable.")
            return None
            
        # Debug info
        st.info(f"Creating embeddings for {len(text_chunks)} text chunks with API key: {api_key[:4]}...")
        
        # Create embeddings
        embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        
        # Create vector store
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
        
        return vectorstore
    except Exception as e:
        st.error(f"Error creating vector store: {str(e)}")
        return None

def get_conversation_chain():
    """
    Create a conversational chain using OpenAI.
    
    Returns:
        chain: Conversational retrieval chain for answering questions
    """
    if not PDF_DEPENDENCIES_LOADED:
        st.error("Required PDF dependencies are not loaded.")
        return None
        
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("OpenAI API key is missing. Please set the OPENAI_API_KEY environment variable.")
            return None
            
        # Debug info
        st.info(f"Creating conversation chain with OpenAI model using API key: {api_key[:4]}...")
        
        # Define the prompt template for the dermatologist assistant
        template = """
        You are a dermatologist AI assistant. Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Always maintain a professional and medical tone. Include relevant medical details when available.
        
        {context}
        
        Question: {question}
        Conversation history: {chat_history}
        """
        
        # Create a prompt from the template
        prompt = PromptTemplate(
            input_variables=["context", "question", "chat_history"],
            template=template
        )
        
        # Use the gpt-4o model (newest model)
        # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # do not change this unless explicitly requested by the user
        llm = ChatOpenAI(
            openai_api_key=api_key,
            model="gpt-4o",
            temperature=0.3
        )
        
        # Create memory for conversation history
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Create the conversational retrieval chain
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=None,  # Will be set later
            memory=memory,
            combine_docs_chain_kwargs={"prompt": prompt}
        )
        
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
        chain: Conversational retrieval chain for answering questions
        
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
        
        # Set the retriever for the chain if not already set
        if chain.retriever is None:
            chain.retriever = vector_store.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 4}  # Return top 4 most similar chunks
            )
        
        # Process the question
        response = chain.invoke({"question": user_question})
        
        # Debug info about response type
        st.info(f"Response received from OpenAI")
        
        # Extract the content from the response
        if isinstance(response, dict) and "answer" in response:
            return response["answer"]
        else:
            # Return the full response for debugging
            return str(response)
    except Exception as e:
        st.error(f"Error processing question: {str(e)}")
        return f"I'm having trouble processing your question: {str(e)}. Please try again or upload a different document."