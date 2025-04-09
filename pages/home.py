import streamlit as st
from utils.styles import load_css
from utils.disease_data import get_disease_cards_data

def show_home():
    """Display the home page of the application."""
    
    # Load custom CSS
    st.markdown(load_css(), unsafe_allow_html=True)
    
    # Main header
    st.markdown(
        f"<h1 class='main-header' style='text-align: center;'>👋 Welcome to <span style='color:#E74C3C;'>TelidermAI</span></h1>", 
        unsafe_allow_html=True
    )
    
    # Introduction
    st.markdown(
        """
        <p style='text-align: center; font-size: 18px;'>
            TelidermAI is an <strong>AI-driven dermatology assistant</strong> designed to provide 
            early insights into your skin health. Using advanced deep learning, it helps users 
            assess potential skin conditions and gain access to valuable dermatological knowledge.
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    # Main feature buttons section
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    
    # Create a two-column layout for the feature buttons
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div class='feature-box'>
                <h3>📷 Image Prediction</h3>
                <p>Upload a photo of your skin condition and get instant AI-powered diagnostic suggestions. Our model has been trained on thousands of dermatological images to provide accurate preliminary assessments.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        # Button to update session state directly
        if st.button("Go to Image Prediction", key="predict_button", use_container_width=True):
            st.session_state['current_page'] = 'Predict'
            st.rerun()
    
    with col2:
        st.markdown(
            """
            <div class='feature-box'>
                <h3>💬 Chat with PDF</h3>
                <p>Upload dermatology PDFs and ask questions using our smart Q&A system powered by Google's Gemini AI. Get specific information from your documents through natural language conversations.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        # Button to update session state directly
        if st.button("Go to Chat with PDF", key="chat_button", use_container_width=True):
            st.session_state['current_page'] = 'Chat with PDF'
            st.rerun()
    
    # Disease Cards Section
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    st.markdown(
        f"<h2 style='color: #611e9e; text-align: center;'>Common Skin Conditions</h2>", 
        unsafe_allow_html=True
    )
    
    # Create three columns for the first row of disease cards
    col1, col2, col3 = st.columns(3)
    
    # Get disease data
    diseases = get_disease_cards_data()
    
    # Display the first three disease cards in the first row
    for i, col in enumerate([col1, col2, col3]):
        if i < len(diseases):
            with col:
                disease = diseases[i]
                st.markdown(
                    f"""
                    <div class='disease-card'>
                        <h3>{disease['name']}</h3>
                        <p>{disease['description']}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
    
    # Create three columns for the second row of disease cards
    col4, col5, col6 = st.columns(3)
    
    # Display the remaining disease cards in the second row
    for i, col in enumerate([col4, col5, col6]):
        j = i + 3
        if j < len(diseases):
            with col:
                disease = diseases[j]
                st.markdown(
                    f"""
                    <div class='disease-card'>
                        <h3>{disease['name']}</h3>
                        <p>{disease['description']}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
    
    # Important note section
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    st.markdown(
        f"<h2 style='color: #611e9e; text-align: center;'>⚠️ Important Note:</h2>", 
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p style='text-align: center; font-size: 18px; color: #E74C3C;'>
            TelidermAI is intended for <strong>informational purposes only</strong> and is 
            <strong>not a substitute</strong> for professional medical advice.<br>
            Always consult a certified dermatologist for an accurate diagnosis and treatment.
        </p>
        """, 
        unsafe_allow_html=True
    )
