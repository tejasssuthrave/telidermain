import streamlit as st
# Page config must be the first Streamlit command
st.set_page_config(
    page_title="Telidermai", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide the sidebar completely and other UI elements with custom CSS
st.markdown("""
    <style>
        [data-testid="collapsedControl"] {display: none !important;}
        section[data-testid="stSidebar"] {display: none !important;}
        button[kind="header"] {display: none !important;}
        #MainMenu {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        div.block-container {padding-top: 0 !important;}
    </style>
""", unsafe_allow_html=True)

import streamlit.components.v1 as components
import base64
import os

# Try to import optional dependencies silently
try:
    from PIL import Image
except ImportError:
    Image = None

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv():
        pass

# Don't import torch directly here to avoid conflicts
torch = None
try:
    # Check if torch is available without importing it at module level
    import importlib.util
    if importlib.util.find_spec("torch"):
        # Only use torch indirectly through utils.model_utils
        pass
except Exception:
    pass

# Load environment variables
load_dotenv()

# Check if GOOGLE_API_KEY is set silently
has_api_key = os.getenv("GOOGLE_API_KEY") is not None

# Import utility modules
from utils.model_utils import load_model

# Import page modules
from pages.home import show_home
from pages.about import show_about
from pages.predict import show_predict
from pages.chat_with_pdf import show_chat_with_pdf
from pages.how_to_use import show_how_to_use
from pages.contact_us import show_contact_us
# from pages.predict import show_predict

# --- Logo and Top Bar ---
LOGO_PATH = "Red_Circle_Health_Logo-removebg-preview.png"  # Using the updated logo
github_url = "https://github.com/123-rishi/Teliderm-Ai"
huggingface_url = "https://huggingface.co/tejasssuthrave/telidermai"
contact_url = "tel:+918296984321"
email_address = "mailto:telidermai@gmail.com"
icon_size = "1.2em"

github_icon_html = f'<a href="{github_url}" target="_blank" style="margin-left: 10px; text-decoration: none; font-size: {icon_size}; color: #611e9e;"><i class="fab fa-github"></i></a>'
huggingface_icon_html = f'<a href="{huggingface_url}" target="_blank" style="margin-left: 20px; text-decoration: none; font-size: {icon_size}; color: #611e9e;">HF</a>'
email_icon_html = f'<a href="{email_address}" style="margin-left: 20px; text-decoration: none; font-size: {icon_size}; color: #611e9e;"><i class="fas fa-envelope"></i></a>'
contact_icon_html = f'<a href="{contact_url}" style="margin-left: 20px; text-decoration: none; font-size: {icon_size}; color: #611e9e;"><i class="fas fa-phone"></i></a>'

def get_base64_of_image(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Error: Logo file not found at {path}")
        return None

logo_html = ""
logo_base64 = get_base64_of_image(LOGO_PATH)
if logo_base64:
    logo_html = f'<img src="data:image/png;base64,{logo_base64}" style="height: 130px; margin-right: 15px;">'
else:
    logo_html = '<span style="font-size: 1.5em; font-weight: bold; margin-right: 15px;">TelidermAI</span>'

subheading = "<h5 style='color: #8149b5; margin-top: 0; margin-bottom: 0;'>Your Virtual Guide for Primary Skin Condition Examination Using Images 🩺🔍</h5>"

top_bar_html_with_logo_subheading = f"""
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" 
          integrity="sha512-9usAa10IRO0HhonpyAIVpjrylPvoDwiPUiKdWk5t3PyolY1cOd4DSE0Ga+ri4AuTroPR5aQvXU9xC6qOPnzFeg==" 
          crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 20px;">
    <div style="display: flex; align-items: center;">
        {logo_html}
        <div>
            <h1 style="color: #611e9e; margin-bottom: 5px;">TelidermAI</h1>
            {subheading}
        </div>
    </div>
    <div>
        {github_icon_html}
        {huggingface_icon_html}
        {email_icon_html}
        {contact_icon_html}
    </div>
</div>
"""

st.markdown(top_bar_html_with_logo_subheading, unsafe_allow_html=True)

# --- Session State Initialization ---
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'Home'
    
if 'model' not in st.session_state:
    # Load model at startup to avoid reloading
    processor, model, device = load_model()
    st.session_state['processor'] = processor
    st.session_state['model'] = model
    st.session_state['device'] = device

# --- Styling ---
primary_color = "#611e9e"
secondary_color = "#6c757d"
background_light = "#f8f9fa"
background_dark = "#212529"
text_light = "#212529"
text_dark = "#f8f9fa"
accent_color = "#4d177a"

st.markdown(f"""<style>
/* Hide Streamlit's default header, footer, and menu */
header {{visibility: hidden;}}
footer {{visibility: hidden;}}
#MainMenu {{visibility: hidden;}}

/* Base body styling */
body {{
    background-color: {background_light};
    color: {text_light};
    margin: 0;
    padding: 0;
    font-family: 'Roboto', sans-serif;
}}

@media (prefers-color-scheme: dark) {{
    body {{
        background-color: {background_dark};
        color: {text_dark};
    }}
}}

/* Top bar styling */
div[style*="display: flex; justify-content: space-between; align-items: center; padding: 10px 20px;"] {{
    margin-bottom: 10px !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-bottom: 3px solid {primary_color};
}}

/* Navigation bar styling */
.nav-container {{
    margin-top: 10px !important;
    margin-bottom: 25px !important;
    padding-top: 0 !important;
    border-radius: 0;
    background: none;
    padding: 10px !important;
}}

/* Button styling */
.stButton>button {{
    background-color: {primary_color} !important;
    color: white !important;
    border-radius: 8px !important;
    border: none;
    padding: 10px 15px;
    font-weight: bold;
    transition: all 0.3s ease;
    width: 100%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}}

.stButton>button:hover {{
    background-color: {accent_color} !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}}

/* Headers styling */
.main-header {{
    color: {primary_color};
    margin-bottom: 0.5em;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}}

h2, h3, h4, h5, h6 {{
    color: {primary_color};
}}

h4[style*="color: #611e9e;"] {{
    margin-top: 2px !important;
    margin-bottom: 5px !important;
}}

/* Container spacing */
.st-container {{
    padding-top: 20px !important;
}}

/* Link styling */
a {{
    color: {primary_color};
    text-decoration: none;
    transition: all 0.2s ease;
}}

a:hover {{
    text-decoration: underline;
    color: {accent_color};
}}

/* Info and warning boxes */
.info-box {{
    background-color: #e9ecef;
    color: {text_light};
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 15px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    border-left: 4px solid {primary_color};
}}

@media (prefers-color-scheme: dark) {{
    .info-box {{
        background-color: #495057;
        color: {text_dark};
    }}
}}

.warning-box {{
    background-color: #fff3cd;
    color: #856404;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 15px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    border-left: 4px solid #ffc107;
}}

@media (prefers-color-scheme: dark) {{
    .warning-box {{
        background-color: #66570a;
        color: #fff3cd;
    }}
}}

/* Image containers */
.uploaded-image-container-inline {{
    display: inline-block;
    margin-right: 10px;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}}

.uploaded-image-container-inline:hover {{
    transform: scale(1.02);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}}

/* File uploader styling */
.st-bq {{
    border-radius: 10px !important;
    border: 2px dashed {primary_color} !important;
    padding: 20px !important;
}}

/* Text input styling */
.st-c8, .st-c9, .st-b8, .st-b9 {{
    border-radius: 8px !important;
    border: 1px solid #ccc !important;
}}

/* Custom widgets styling */
.stSlider {{
    padding-top: 10px !important;
    padding-bottom: 10px !important;
}}

.stProgress > div > div {{
    background-color: {primary_color} !important;
}}

/* Improved streamlit default component styling */
.css-1aumxhk {{
    background-color: #ffffff;
    border-radius: 10px !important;
    padding: 15px !important;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05) !important;
    margin-bottom: 20px !important;
}}

/* Expander styling */
.st-eb {{
    border-radius: 10px !important;
    border: none !important;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05) !important;
}}

.st-fh {{
    color: {primary_color} !important;
    font-weight: bold !important;
}}
</style>""", unsafe_allow_html=True)

# --- Navigation Bar ---
def create_nav_bar():
    menu_items = ["Home", "About", "Predict", "Chat with PDF", "How to Use", "Contact Us"]
    
    # Create columns for each menu item
    nav_cols = st.columns(len(menu_items))
    
    # Add styling container
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    
    # Display buttons in the navigation bar
    for idx, item in enumerate(menu_items):
        with nav_cols[idx]:
            if st.button(item, key=f"nav_{item}"):
                st.session_state['current_page'] = item
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Display navigation bar
create_nav_bar()

# --- Check URL parameters for page navigation ---
try:
    # Use newer query_params method to avoid deprecation warning
    query_params = st.query_params
    if "page" in query_params:
        page_from_url = query_params["page"].lower()
        if page_from_url == "predict":
            st.session_state['current_page'] = 'Predict'
        elif page_from_url == "chat_with_pdf":
            st.session_state['current_page'] = 'Chat with PDF'
        elif page_from_url == "about":
            st.session_state['current_page'] = 'About'
        elif page_from_url == "how_to_use":
            st.session_state['current_page'] = 'How to Use'
        elif page_from_url == "contact_us":
            st.session_state['current_page'] = 'Contact Us'
except:
    # Fallback to experimental method if the new one isn't available
    try:
        query_params = st.experimental_get_query_params()
        if "page" in query_params:
            page_from_url = query_params["page"][0].lower()
            if page_from_url == "predict":
                st.session_state['current_page'] = 'Predict'
            elif page_from_url == "chat_with_pdf":
                st.session_state['current_page'] = 'Chat with PDF'
            elif page_from_url == "about":
                st.session_state['current_page'] = 'About'
            elif page_from_url == "how_to_use":
                st.session_state['current_page'] = 'How to Use'
            elif page_from_url == "contact_us":
                st.session_state['current_page'] = 'Contact Us'
    except:
        pass  # If neither method works, just continue with the current page

# --- Page Routing Based on Session State ---
if st.session_state['current_page'] == 'Home':
    show_home()
elif st.session_state['current_page'] == 'About':
    show_about()
elif st.session_state['current_page'] == 'Predict':
    show_predict(st.session_state['processor'], st.session_state['model'], st.session_state['device'])
elif st.session_state['current_page'] == 'Chat with PDF':
    from pages.new_pdf_chat import show_new_pdf_chat
    show_new_pdf_chat()
elif st.session_state['current_page'] == 'How to Use':
    show_how_to_use()
elif st.session_state['current_page'] == 'Contact Us':
    show_contact_us()

# Add footer at the absolute bottom of the page
st.markdown(
    """
    <style>
    html, body, .main {
        height: 100%;
        margin: 0;
        padding: 0;
    }

    .main {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .footer {
        width: 100%;
        background-color: #611e9e;
        padding: 10px;
        left: 0;
        text-align: center;
        color: white;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        margin-top: 30px;
    }

    /* Remove unwanted bottom spacing */
    .block-container {
        padding-bottom: 0 !important;
    }
    </style>

    <div class="footer">
        <p style="margin: 0; padding: 5px; font-size: 14px;">
            TelidermAI - Your Virtual Guide for Primary Skin Condition Examination © 2025
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
