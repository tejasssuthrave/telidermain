import streamlit as st
import os
import time
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def show_new_pdf_chat():
    """Display a simple PDF chat interface using direct Google Gemini API in a two-column layout."""
    
    # Function to extract text from PDFs - defined first to fix the reference error
    def extract_text_from_pdfs(pdf_files):
        text = ""
        for pdf in pdf_files:
            try:
                pdf_reader = PdfReader(pdf)
                for page in pdf_reader.pages:
                    text += page.extract_text() or ""
            except Exception as e:
                st.error(f"Error processing {pdf.name}: {str(e)}")
        return text
    
    # Function to split text into chunks - defined first to fix the reference error
    def split_text_into_chunks(text, chunk_size=4000, chunk_overlap=200):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )
        return text_splitter.split_text(text)

    # Page title with styled heading
    st.markdown(
        "<h1 style='text-align: center; color: #611e9e;'>📄 Chat with PDF</h1>", 
        unsafe_allow_html=True
    )
    
    # Introduction
    st.write("Upload PDF documents related to dermatology and ask questions to get information.")
    
    # Check for Google API key silently
    api_key = os.getenv("GOOGLE_API_KEY")
    has_api_key = api_key is not None
    
    if not has_api_key:
        st.error("""
        **Google API Key Missing**: This feature requires a Google API Key to function properly.
        Please contact the administrator to set up the GOOGLE_API_KEY environment variable.
        """)
    
    # Initialize session state
    if "pdf_text" not in st.session_state:
        st.session_state.pdf_text = ""
    if "pdf_chunks" not in st.session_state:
        st.session_state.pdf_chunks = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Create a two-column layout with equal width columns
    col1, col2 = st.columns(2)
    
    # Left column for file upload
    with col1:
        st.markdown("<h3 style='color: #611e9e;'>Upload your PDF Files</h3>", unsafe_allow_html=True)
        pdf_docs = st.file_uploader(
            "Drag and drop files here",
            accept_multiple_files=True,
            type=["pdf"],
            help="Limit 200MB per file • PDF"
        )
        
        # Process PDFs button
        if pdf_docs:
            if st.button("Process PDFs", type="primary", help="Extract text from uploaded PDFs", use_container_width=True):
                with st.spinner("Processing your documents..."):
                    # Show progress
                    progress_bar = st.progress(0)
                    time.sleep(0.5)
                    progress_bar.progress(30)
                    
                    # Extract text
                    st.session_state.pdf_text = extract_text_from_pdfs(pdf_docs)
                    
                    progress_bar.progress(60)
                    
                    # Split into chunks
                    if st.session_state.pdf_text:
                        st.session_state.pdf_chunks = split_text_into_chunks(st.session_state.pdf_text)
                    
                    progress_bar.progress(100)
                    time.sleep(0.5)
                    
                    if st.session_state.pdf_text.strip():
                        # Display success and text length
                        doc_length = len(st.session_state.pdf_text)
                        chunk_count = len(st.session_state.pdf_chunks)
                        st.success(f"✅ Successfully extracted {doc_length} characters from {len(pdf_docs)} PDF document(s) and created {chunk_count} chunks.")
                        
                        # Clear previous conversation
                        st.session_state.chat_history = []
                    else:
                        st.error("⚠️ Could not extract any text from the uploaded PDFs. Please try different files.")
    
    # Removing duplicate functions since they're already defined at the top
    
    # Function to get response using LangChain with the correct model
    def get_ai_response(question, context):
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                return "API key is missing. Cannot generate response."
            
            # Create prompt
            prompt_template = f"""
            You are a medical professional specializing in dermatology. 
            Answer the following question based on the context provided. 
            If the answer is not in the context, say that you don't have that information.
            Be professional and concise in your response.
            
            Context: {context}
            
            Question: {question}
            """
            
            # Use the specific model version requested
            model = ChatGoogleGenerativeAI(
                model="gemini-1.5-pro",
                google_api_key=api_key,
                temperature=0.3
            )
            
            response = model.invoke(prompt_template)
            return response.content
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    # This duplicate button should be deleted since we already moved it to the left column
    # Removing this block to avoid duplicate buttons
    
    # Right column for instructions or conversation
    with col2:
        # Always display usage instructions, even after PDFs are processed
        st.markdown("<h3 style='color: #611e9e;'>How to use PDF Chat</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px;">
                <ol>
                    <li><strong>Upload Documents:</strong> Start by uploading one or more PDF files containing dermatology information.</li>
                    <li><strong>Process the PDFs:</strong> Click the "Process PDFs" button to extract the text content.</li>
                    <li><strong>Ask Questions:</strong> Once processing is complete, you can ask questions about the content of your documents.</li>
                </ol>
                <p>The AI assistant will analyze your documents and provide relevant information based on your questions.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        # Show example image of PDF chat in action
        st.markdown("<h4 style='color: #611e9e; margin-top: 20px;'>Example PDF Analysis</h4>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #611e9e;">
                <p><strong>Functionality:</strong> Upload medical PDFs and get AI-powered answers about skin conditions.</p>
                <p><strong>Ideal for:</strong> Medical students, dermatologists, or anyone researching skin conditions.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
            
    # After PDFs have been processed, show the chat interface below both columns
    if st.session_state.pdf_chunks:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #611e9e; text-align: center;'>Ask Questions About Your Documents</h3>", unsafe_allow_html=True)
        
        # Define a function to process the user question
        def process_user_question():
            if not has_api_key:
                st.error("Cannot process question without a Google API key.")
            elif not st.session_state.user_question:
                st.warning("Please enter a question.")
            else:
                with st.spinner("Processing your question..."):
                    # Find relevant chunks for the question
                    # Join all chunks but limit context size to avoid token limits
                    max_context_size = 12000
                    context = " ".join(st.session_state.pdf_chunks)
                    if len(context) > max_context_size:
                        context = context[:max_context_size]
                    
                    # Get response from AI
                    response = get_ai_response(st.session_state.user_question, context)
                    
                    # Add to conversation history (newest messages first)
                    st.session_state.chat_history.insert(0, {"role": "assistant", "content": response})
                    st.session_state.chat_history.insert(0, {"role": "user", "content": st.session_state.user_question})
                    
                    # Clear the input field after submission
                    st.session_state.user_question = ""
        
        # Initialize the session state for the text input if it doesn't exist
        if "user_question" not in st.session_state:
            st.session_state.user_question = ""
            
        # Text input for user question with on_change callback to detect Enter key
        user_question = st.text_area(
            "Ask a question about your dermatology documents:",
            height=100,
            placeholder="For example: What are the symptoms of eczema? (Press Enter to submit)",
            key="user_question"
        )
        
        # Create columns for spacing the button
        col1, col2, col3 = st.columns([1, 1, 1])
        
        # Submit button in the middle column
        with col2:
            if st.button("Submit Question", type="primary", use_container_width=True, on_click=process_user_question):
                pass  # The on_click handler will take care of processing
        
        # Display conversation
        if st.session_state.chat_history:
            st.markdown("<h3 style='color: #611e9e; text-align: center;'>Conversation</h3>", unsafe_allow_html=True)
            
            # Create a container for the chat with fixed height and scrolling
            chat_container = st.container(height=400, border=False)
            
            with chat_container:
                # The chat history is already in reversed order (newest messages first)
                for message in st.session_state.chat_history:
                    if message["role"] == "user":
                        st.markdown(
                            f"""
                            <div style='display: flex; justify-content: flex-end; margin-bottom: 10px;'>
                                <div style='background-color: #F0F2F6; padding: 10px 15px; border-radius: 20px 20px 0px 20px; max-width: 80%; box-shadow: 0px 1px 2px rgba(0,0,0,0.1);'>
                                    <p style='margin: 0; font-weight: bold;'>You</p>
                                    <p style='margin: 0;'>{message['content']}</p>
                                </div>
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f"""
                            <div style='display: flex; justify-content: flex-start; margin-bottom: 10px;'>
                                <div style='background-color: #E8DEF8; padding: 10px 15px; border-radius: 20px 20px 20px 0px; max-width: 80%; box-shadow: 0px 1px 2px rgba(0,0,0,0.1);'>
                                    <p style='margin: 0; font-weight: bold; color: #611e9e;'>AI</p>
                                    <p style='margin: 0;'>{message['content']}</p>
                                </div>
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
            
            # Action buttons below chat
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Clear Conversation", type="secondary", use_container_width=True):
                    st.session_state.chat_history = []
                    st.rerun()
            with col2:
                if st.button("Start New Analysis", type="secondary", use_container_width=True):
                    st.session_state.pdf_text = ""
                    st.session_state.pdf_chunks = []
                    st.session_state.chat_history = []
                    st.rerun()