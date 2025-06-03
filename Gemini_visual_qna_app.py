import streamlit as st
from PIL import Image, UnidentifiedImageError
import google.generativeai as genai
import os

# App title and layout
st.set_page_config(page_title="Gemini Visual QnA Chatbot", layout="wide")
st.title("🖼️ Gemini Multimodal Visual QnA Chatbot")
st.markdown("Upload any image (chart, infographic, artwork, diagram, etc.) and ask a question about it.")

# Get API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Set up Gemini model
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
uploaded_file = st.file_uploader("Upload an image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file and api_key:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
    except UnidentifiedImageError:
        st.error("❌ The uploaded file is not a valid image. Please upload a PNG, JPG, or JPEG.")
        st.stop()
    except Exception as e:
        st.error("❌ An unexpected error occurred while loading the image.")
        st.exception(e)
        st.stop()

    model = setup_model(api_key)

    with st.form("question_form"):
        prompt = st.text_input("Ask a question about the image:", placeholder="e.g., What does this diagram show?")
        submitted = st.form_submit_button("Generate Response")

    if submitted and prompt:
        with st.spinner("Generating response..."):
            try:
                response = model.generate_content([prompt, image])
                st.markdown("### 🤖 Gemini Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.write("Full error log:")
                st.exception(e)
else:
    st.info("Please upload an image and ensure the Gemini API key is setup in the Streamlit Cloud secrets.")