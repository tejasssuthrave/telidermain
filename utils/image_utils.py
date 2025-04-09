from PIL import Image, ImageOps
import streamlit as st
import torch

def prepare_image(uploaded_file, target_size=(224, 224)):
    """
    Prepare an uploaded image for model prediction.
    
    Args:
        uploaded_file: The uploaded image file
        target_size: Target size for model input
        
    Returns:
        tuple: (display_image, model_input_image) - Image for display and for model input
    """
    try:
        # Open the image and convert to RGB
        image = Image.open(uploaded_file).convert("RGB")
        
        # Create a smaller version for display
        max_display_size = (300, 300)
        display_image = image.copy()
        display_image.thumbnail(max_display_size)
        
        # Create a properly sized and formatted version for the model
        model_input_image = ImageOps.fit(image, target_size)
        
        return display_image, model_input_image
        
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
        return None, None
