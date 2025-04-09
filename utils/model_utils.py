import torch
import torch.nn.functional as F
from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image, ImageOps
import streamlit as st

@st.cache_resource
def load_model():
    """Loads the ViT model and processor."""
    model_name = "tejasssuthrave/telidermai"  # Your model
    try:
        processor = ViTImageProcessor.from_pretrained(model_name)
        model = ViTForImageClassification.from_pretrained(model_name)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model.to(device)
        model.eval()
        st.info(f"Model '{model_name}' loaded successfully on {device.upper()}")
        return processor, model, device
    except Exception as e:
        st.error(f"Error loading model '{model_name}': {e}")
        return None, None, None

def predict_skin_condition(image, processor, model, device, top_n=3):
    """
    Process image and predict skin condition using the loaded model.

    Args:
        image: PIL image
        processor: ViT image processor
        model: ViT model
        device: Device to run inference on
        top_n: Number of top predictions to return

    Returns:
        tuple: (predicted_class_label, top_n_predictions) - The top prediction and the top N predictions
    """
    if processor is None or model is None or device is None:
        st.error("Model or processor not loaded. Please check the loading process.")
        return "Error", []

    try:
        image = image.convert("RGB")
        image = ImageOps.fit(image, (224, 224))
        inputs = processor(images=image, return_tensors="pt").to(device)

        with torch.no_grad():
            outputs = model(**inputs)
            probabilities = F.softmax(outputs.logits, dim=-1)
            predicted_class_index = torch.argmax(outputs.logits, dim=-1).item()

        predicted_class_label = model.config.id2label.get(predicted_class_index, "Unknown")

        sorted_indices = torch.argsort(probabilities, dim=-1, descending=True).squeeze().cpu().numpy().tolist()
        top_n_predictions = []
        probabilities_cpu = probabilities.squeeze().cpu().numpy()
        labels = model.config.id2label

        for i in range(min(top_n, len(sorted_indices))):
            index = sorted_indices[i]
            confidence = probabilities_cpu[index] * 100
            label = labels.get(index, f"Class {index}")
            top_n_predictions.append({"label": label, "confidence": confidence})

        return predicted_class_label, top_n_predictions

    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return "Error", []
