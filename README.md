# 📊 Gemini Multimodal Visual QnA Chatbot App

An interactive **Streamlit app** that uses **Google Gemini Pro** (`gemini-1.5-flash`) to perform **visual question answering**. Upload any image (balance sheet, KPI chart, report, etc.), ask natural language questions, and receive smart structured responses from Gemini.

---

## 🚀 Features
- 📷 Upload image files (JPEG, PNG)
- 💬 Ask any question about the image (e.g., "Summarize in 5 bullet points")
- 🤖 Get AI-powered insights via Google Gemini
- 🌐 Deploys on Streamlit Cloud in seconds

---

## 📸 App Demo

### 1. Uploading an Image
![App UI](screenshots/app_ui.png)

### 2. Gemini's Response
![Response Demo](screenshots/app_ui_gemini_response.png)

---

## 🛠️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Gemini-Multimodal-App.git
cd Gemini-Multimodal-App
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run Gemini_visual_qna_app.py
```

### 4. API Key

This app uses Gemini-1.5 Flash model from Google’s Gemini API.  
To run the app yourself, store your API key in **Streamlit Secrets**:

```
GEMINI_API_KEY = "your-google-api-key"
```

> 🔒 The key is accessed securely via `st.secrets["GEMINI_API_KEY"]`.  
> No key input is required in the app UI.

---

## 📚 Technologies Used
- [Streamlit](https://streamlit.io/)
- [Google Generative AI SDK](https://ai.google.dev/gemini-api/docs)
- [Pillow](https://python-pillow.org/)

---

## 📄 License
MIT License © 2025 Sanjana Shah

---

## 👤 Author

**Sanjana Shah**  
✨ Machine Learning & Generative AI Enthusiast  
📫 Connect on [LinkedIn](https://www.linkedin.com/in/sanjanavshah)
GitHub: [@shahsanjanav](https://github.com/shahsanjanav)

---

⭐ If you like this project, consider starring it on GitHub!
