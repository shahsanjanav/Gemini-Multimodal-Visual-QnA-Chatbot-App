import streamlit as st
from PIL import Image
import google.generativeai as genai
import os

# App title and sidebar
st.set_page_config(page_title="Gemini Financial Analyzer", layout="wide")
st.title("📊 Gemini Multimodal Financial Insight App")
st.markdown("Ask questions about your uploaded financial image.")

# Input: API Key (hide for deployment)
st.sidebar.title("🔐 API Key")
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

# Set up model
@st.cache_resource
def setup_model(api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"temperature": 0.4, "top_p": 1, "max_output_tokens": 4096},
        safety_settings=[
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ]
    )
    return model

# Upload image
uploaded_file = st.file_uploader("Upload a financial report image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    model = setup_model(api_key)

    with st.form("question_form"):
        prompt = st.text_input("Ask a question about the image:", placeholder="e.g., Summarize key insights in 5 bullet points")
        submitted = st.form_submit_button("Generate Response")

    if submitted and prompt:
        with st.spinner("Generating response..."):
            try:
                response = model.generate_content([prompt, image])
                st.markdown("### 🤖 Gemini Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
                st.write("Full error log:")
                st.exception(e)
else:
    st.info("Please upload an image and enter your API key to begin.")