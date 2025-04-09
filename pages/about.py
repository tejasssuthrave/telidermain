import streamlit as st

def show_about():
    """Display the about page with information about the application and the team."""
    
    # Define colors for the page
    primary_purple = "#6A0DAD"
    secondary_purple = "#D8BFD8"
    background_purple = "#F0E6F8"
    text_dark = "#333"
    text_light = "#4B0082"
    
    # Page header
    st.markdown(
        f"<h1 style='color: {primary_purple};text-align: center;'>ℹ️ About Telidermai</h1>", 
        unsafe_allow_html=True
    )
    
    # About the application
    st.markdown(
        f"""
        <div style="background-color: {background_purple}; padding: 20px; border: 1px solid {secondary_purple}; 
        border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); margin-bottom: 20px;">
            <p style="font-size: 1.1em; line-height: 1.6; color: {text_dark};">
                TeledermAI is a deep learning-based web application developed to assist in the preliminary 
                identification of various skin diseases using dermatoscopic images. It leverages advanced 
                Vision Transformer models trained on a carefully curated dataset of medical images.
            </p>
            <p style="font-size: 1.1em; line-height: 1.6; color: {text_dark};">
                Our mission is to increase accessibility to dermatological expertise, particularly 
                in regions with limited access to healthcare professionals. By providing a preliminary 
                analysis, TeledermAI aims to help users make informed decisions about seeking professional 
                medical advice.
            </p>
            <p style="font-size: 1.1em; line-height: 1.6; color: {text_dark};">
                <strong>Note:</strong> This tool is not intended to replace professional medical 
                diagnosis. Always consult a qualified healthcare provider for proper evaluation and treatment.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
# 👉 Add the disease list HTML block here
    disease_tags_html = """
    <div style="background-color: #F0E6F8; padding: 20px; border: 1px solid #D8BFD8; 
         border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); margin-bottom: 20px;">
         <h2 style="color: #6A0DAD; font-size: 1.5em; margin-bottom: 10px;">Conditions We Detect</h2>
        <p style="font-size: 1.05em; line-height: 1.6; color: #333;">
            TeledermAI is capable of detecting a wide variety of skin conditions, including:
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px;">
            <!-- Paste all the span elements here -->
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Basal Cell Carcinoma</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Darier's Disease</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Epidermolysis Bullosa</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Hailey-Hailey Disease</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Herpes</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Impetigo</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Creeping Eruption</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Borderline Leprosy</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Lepromatous Leprosy</span>    
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Tuberculoid Leprosy</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Lichen Planus</span>
                  <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Discoid Lupus</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Melanoma</span>
                  <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Molluscum</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Cutaneous T-Cell Lymphoma</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Neurofibromatosis</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Reticulated Papillomatosis</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Head Lice</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Pityriasis Rosea</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Actinic Porokeratosis</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Psoriasis</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Ringworm</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Tinea Nigra</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Tungiasis</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Actinic Keratosis</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Dermatofibroma</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Mole (Nevus)</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Benign Pigmented Growth</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Seborrheic Keratosis</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Squamous Cell Carcinoma</span>
                 <span style="background-color: #e6d5f7; padding: 6px 14px; border-radius: 20px; border: 1px solid #D8BFD8; font-size: 0.95em; color: #333;">Vascular Lesion</span>              
        
        </div>
    </div>
    """
    st.markdown(disease_tags_html, unsafe_allow_html=True)


    # Our team section
    st.markdown(
        f"<h2 style='text-align: center; color: {primary_purple};'>Our Team</h2>", 
        unsafe_allow_html=True
    )
    
    st.markdown(
        f"<p style='text-align: center;'><span style='font-size: 1.5em; color: {text_light};'><strong>Introducing the Telidermai Development Team:</strong></p>", 
        unsafe_allow_html=True
    )
    
    # Create 4 columns for team members
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(
            f"""
            <div style="background-color: {background_purple}; color: {text_dark}; padding: 15px; border: 1px solid {secondary_purple}; border-radius: 10px; margin-bottom: 15px; height: 100%;">
                <h4 style="color: {primary_purple};">Tejas S Suthrave</h4>
                <p><strong>Role:</strong> Lead Developer</p>
                <p><strong>Contact:</strong> +91 9353818247</p>
                <p><strong>Mail:</strong> <a href="mailto:tejassuthrave@gmail.com">tejassuthrave@gmail.com</a></p>
                <p><strong>Linkedin:</strong> <a href="https://www.linkedin.com/in/tejas-s-suthrave-555rag/">tejassuthrave</a></p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f"""
            <div style="background-color: {background_purple}; color: {text_dark}; padding: 15px; border: 1px solid {secondary_purple}; border-radius: 10px; margin-bottom: 15px; height: 100%;">
                <h4 style="color: {primary_purple};">Rohith H</h4>
                <p><strong>Role:</strong> AI Engineer</p>
                <p><strong>Contact:</strong> +91 9876543210</p>
                <p><strong>Mail:</strong> <a href="mailto:rishiiyer875@gmail.com">rishiiyer875@gmail.com</a></p>
                <p><strong>Linkedin:</strong> <a href="https://www.linkedin.com/in/rohith-h-86287a2a2/">rohith h</a></p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            f"""
            <div style="background-color: {background_purple}; color: {text_dark}; padding: 15px; border: 1px solid {secondary_purple}; border-radius: 10px; margin-bottom: 15px; height: 100%;">
                <h4 style="color: {primary_purple};">Vishwas V</h4>
                <p><strong>Role:</strong> Frontend Designer</p>
                <p><strong>Contact:</strong> +91 9765432109</p>
                <p><strong>Mail:</strong> <a href="mailto:priya@example.com">priya@example.com</a></p>
                <p><strong>Linkedin:</strong> <a href="https://www.linkedin.com/in/vishwas-v-446a12285/">vishwas v</a></p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col4:
        st.markdown(
            f"""
            <div style="background-color: {background_purple}; color: {text_dark}; padding: 15px; border: 1px solid {secondary_purple}; border-radius: 10px; margin-bottom: 15px; height: 100%;">
                <h4 style="color: {primary_purple};">Teju B</h4>
                <p><strong>Role:</strong> Backend Developer</p>
                <p><strong>Contact:</strong> +91 9654321098</p>
                <p><strong>Mail:</strong> <a href="mailto:avinash@example.com">avinash@example.com</a></p>
                <p><strong>Linkedin:</strong> <a href="https://www.linkedin.com/in/teju-teju-115ba72b8/">teju b</a></p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # Technology stack section
    st.markdown(
        f"<h2 style='text-align: center; color: {primary_purple};'>Technology Stack</h2>", 
        unsafe_allow_html=True
    )
    
    # Create two columns for technology sections
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            f"""
            <div style="background-color: {background_purple}; color: {text_dark}; padding: 15px; border: 1px solid {secondary_purple}; border-radius: 10px;">
                <h4 style="color: {primary_purple};">Frontend</h4>
                <ul>
                    <li>Streamlit - Interactive web interface</li>
                    <li>HTML/CSS - Styling and layout</li>
                    <li>Font Awesome - Icons and visual elements</li>
                </ul>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f"""
            <div style="background-color: {background_purple}; color: {text_dark}; padding: 15px; border: 1px solid {secondary_purple}; border-radius: 10px;">
                <h4 style="color: {primary_purple};">Backend & AI</h4>
                <ul>
                    <li>PyTorch - Deep learning framework</li>
                    <li>Vision Transformer (ViT) - Image classification</li>
                    <li>Google Gemini - PDF document analysis</li>
                    <li>LangChain - Document processing pipeline</li>
                </ul>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # Data sources section
    st.markdown(
        f"<h2 style='text-align: center; color: {primary_purple}; margin-top: 20px;'>Data Sources & Model Training</h2>", 
        unsafe_allow_html=True
    )
    
    st.markdown(
        f"""
        <div style="background-color: {background_purple}; color: {text_dark}; padding: 20px; border: 1px solid {secondary_purple}; border-radius: 10px; margin-top: 10px;">
            <p>The AI model powering TeledermAI was trained on carefully curated datasets from multiple sources:</p>
            <ul>
                <li>HAM10000 - A large collection of dermatoscopic images of common pigmented skin lesions</li>
                <li>ISIC Archive - International Skin Imaging Collaboration's archive of dermoscopic images</li>
                <li>DermNet NZ - A curated collection of clinical dermatology images</li>
            </ul>
            <p>Our Vision Transformer model was fine-tuned with a focus on accuracy and reliability for the most common skin conditions.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
