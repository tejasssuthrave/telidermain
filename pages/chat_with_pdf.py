import streamlit as st
import os
from utils.pdf_utils import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain, process_question

def show_chat_with_pdf():
    """Display the PDF chat page where users can interact with uploaded PDF documents."""

    st.markdown(f"<h1 style='color: #611e9e; text-align: center;'>📄 Chat with PDF</h1>", unsafe_allow_html=True)
    st.write("Upload PDF documents related to dermatology and ask questions to get information.")

    api_key = os.getenv("GOOGLE_API_KEY")
    has_api_key = api_key is not None

    if not has_api_key:
        st.warning("""
        **Google API Key Missing**: This feature requires a Google API Key to function properly.
        Please contact the administrator to set up the GOOGLE_API_KEY environment variable.
        """)
    else:
        st.success(f"Google API Key detected with prefix {api_key[:4]}... ✓")

    pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True, type=["pdf"])

    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = None

    if pdf_docs:
        if st.button("Process PDFs for Chat"):
            with st.spinner("Processing PDFs..."):
                raw_text = get_pdf_text(pdf_docs)

                if not raw_text.strip():
                    st.error("Could not extract any text from the uploaded PDFs. Please try different files.")
                else:
                    text_chunks = get_text_chunks(raw_text)

                    if not text_chunks:
                        st.error("Failed to process the text from PDFs. Please try again.")
                    else:
                        st.session_state.vector_store = get_vector_store(text_chunks)

                        if st.session_state.vector_store:
                            st.session_state.qa_chain = get_conversational_chain()

                            if st.session_state.qa_chain:
                                st.success(f"Successfully processed {len(pdf_docs)} PDF document(s). You can now ask questions!")
                                st.session_state.conversation_history = []
                            else:
                                st.error("Failed to initialize the AI chat model. Please check your API key and try again.")
                        else:
                            st.error("Failed to create embeddings for the documents. Please try again.")

    if st.session_state.vector_store is not None and st.session_state.qa_chain is not None:
        st.subheader("Ask Questions About Your Documents")

        user_question = st.text_input(
            "Ask a question about your dermatology documents:",
            placeholder="For example: What are the symptoms of eczema?"
        )

        if user_question:
            with st.spinner("Generating response..."):
                st.session_state.conversation_history.append({"role": "user", "content": user_question})
                response = process_question(
                    user_question,
                    st.session_state.vector_store,
                    st.session_state.qa_chain
                )
                st.session_state.conversation_history.append({"role": "assistant", "content": response})

        if st.session_state.conversation_history:
            st.subheader("Conversation")

            for i in range(len(st.session_state.conversation_history) - 1, -1, -2):
                try:
                    user_msg = st.session_state.conversation_history[i - 1]
                    ai_msg = st.session_state.conversation_history[i]
                except IndexError:
                    continue

                if ai_msg["role"] == "assistant":
                    st.markdown(
                        f"""
                        <div style='display: flex; justify-content: flex-start; margin-bottom: 10px;'>
                            <div style='background-color: #E8DEF8; padding: 12px; border-radius: 10px; max-width: 70%;'>
                                <strong>AI</strong><br>{ai_msg['content']}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                if user_msg["role"] == "user":
                    st.markdown(
                        f"""
                        <div style='display: flex; justify-content: flex-end; margin-bottom: 10px;'>
                            <div style='background-color: #F0F2F6; padding: 12px; border-radius: 10px; max-width: 70%; text-align: right;'>
                                <strong>You</strong><br>{user_msg['content']}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            if st.button("Clear Conversation"):
                st.session_state.conversation_history = []
                st.rerun()

    elif not pdf_docs:
        st.markdown(
            """
            <div style="background-color: #f0f2f6; padding: 15px; border-radius: 5px; margin: 15px 0;">
                <p style="margin: 0; padding: 0;">
                    Please upload PDF documents containing dermatology information to begin. 
                    Once processed, you can ask questions about the content of these documents.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
