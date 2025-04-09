import streamlit as st
import torch
import torch.nn.functional as F
from PIL import Image, ImageOps
from utils.image_utils import prepare_image
from utils.model_utils import load_model, predict_skin_condition
from utils.disease_info import get_disease_info

# Load the model and processor (do this once at the top level)
processor, model, device = load_model()




def show_predict(processor=processor, model=model, device=device):
    """
    Display the prediction page where users can upload and analyze skin images.

    Args:
        processor: The image processor for the model
        model: The loaded ViT model
        device: The device to run inference on
    """
    # Page header
    st.markdown(f"<h1 class='main-header' style='text-align: center;'>🩺 Image Prediction</h1>", unsafe_allow_html=True)

    # Introduction
    # st.write("Upload an image of a skin condition to get a preliminary AI-powered prediction.")

    # Custom message for better results
    st.markdown(
        """
        <div style="background-color: #f0f2f6; padding: 10px 15px; border-radius: 5px; margin-bottom: 15px;">
            <p style="margin: 0; padding: 0;">Please ensure the image is clear and well-lit for better results.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Load disease information database
    disease_info = get_disease_info()

    # Create a 3-column layout for upload, image display, and prediction results
    col1, col2, col3 = st.columns([1,1,1])

    # Initialize session state variables
    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None
    if 'display_image' not in st.session_state:
        st.session_state.display_image = None
    if 'model_input_image' not in st.session_state:
        st.session_state.model_input_image = None
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'prediction_results' not in st.session_state:
        st.session_state.prediction_results = None
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False

    # Column 1: Upload section
    with col1:
        st.markdown("<h3>Upload Image</h3>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload a skin condition image", type=["jpg", "jpeg", "png"])

        if uploaded_file:
            st.session_state.uploaded_image = uploaded_file
            st.session_state.submitted = False
            st.session_state.prediction_results = None
            st.session_state.show_results = False

        if st.session_state.uploaded_image and not st.session_state.submitted:
            if st.button("Analyze Image", type="primary", use_container_width=True):
                with st.spinner("Processing image..."):
                    try:
                        image = Image.open(st.session_state.uploaded_image)
                        st.session_state.display_image = image
                        st.session_state.model_input_image = image
                        st.session_state.submitted = True
                    except Exception as e:
                        st.error(f"Error processing uploaded image: {e}")

        if st.session_state.submitted:
            if st.button("Reset & Upload New Image", type="secondary", use_container_width=True):
                st.session_state.uploaded_image = None
                st.session_state.display_image = None
                st.session_state.model_input_image = None
                st.session_state.submitted = False
                st.session_state.prediction_results = None
                st.session_state.show_results = False
                st.rerun()

    # Column 2: Image Display
    with col2:
        st.markdown("<h3>Uploaded Image</h3>", unsafe_allow_html=True)
        display_placeholder = st.empty()

        if st.session_state.uploaded_image:
            try:
                img = Image.open(st.session_state.uploaded_image)
                display_placeholder.image(
                    img,
                    caption="Your uploaded image",
                    width=350
                )
            except Exception as e:
                display_placeholder.error(f"Error displaying image: {e}")
        else:
            display_placeholder.markdown(
                """
                <div style="border: 1px dashed #ccc; border-radius: 5px; padding: 20px; text-align: center; color: #888;">
                    <p>Uploaded image will appear here after you submit the image</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Column 3: Prediction Results
    with col3:
        st.markdown("<h3>Prediction Results</h3>", unsafe_allow_html=True)
        results_placeholder = st.empty()

        if st.session_state.submitted and st.session_state.model_input_image and not st.session_state.prediction_results:
            try:
                with st.spinner("Analyzing image..."):
                    predicted_class, top_predictions = predict_skin_condition(
                        st.session_state.model_input_image, processor, model, device
                    )
                    st.session_state.prediction_results = {
                        "predicted_class": predicted_class,
                        "top_predictions": top_predictions
                    }
                    st.session_state.show_results = True
            except Exception as e:
                results_placeholder.error(f"Error during prediction: {str(e)}")

        if st.session_state.show_results and st.session_state.prediction_results:
            predicted_class = st.session_state.prediction_results["predicted_class"]
            top_predictions = st.session_state.prediction_results["top_predictions"]

            with results_placeholder.container():
                st.markdown(
                    f"<h4 style='color: #611e9e;'>Top Prediction:</h4>"
                    f"<p style='font-size: 1.2em; font-weight: bold;'>{predicted_class}</p>",
                    unsafe_allow_html=True
                )

                st.markdown("<h4>Confidence Scores:</h4>", unsafe_allow_html=True)
                for pred in top_predictions:
                    st.markdown(f"**{pred['label']}**")
                    st.progress(pred['confidence'] / 100)
                    st.write(f"{pred['confidence']:.2f}%")
        elif st.session_state.submitted and not st.session_state.prediction_results:
            results_placeholder.info("Analyzing image...")
        else:
            results_placeholder.markdown(
                """
                <div style="border: 1px dashed #ccc; border-radius: 5px; padding: 20px; text-align: center; color: #888;">
                    <p>Prediction results will appear here after image analysis</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Medical Disclaimer
    st.markdown("---")
    st.markdown(
        """
        <div style="background-color: #ffecb3; padding: 10px 15px; border-radius: 5px; margin-bottom: 15px;">
            <p style="margin: 0; padding: 0; color: #7d4e00; font-weight: bold;">
                ⚠️ <strong>Medical Disclaimer</strong>: This prediction is for informational purposes only and should not
                replace professional medical advice. If you're concerned about a skin condition, please consult
                with a qualified healthcare provider. Seek immediate medical attention if your condition worsens or
                if you experience severe symptoms.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
