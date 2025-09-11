---
title: Gemini Streamlit Chatbot
emoji: 🦜
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.38.0"
app_file: streamlit_app.py
pinned: false
---

# 🦜🔗 Gemini Streamlit Chatbot

This is a simple Streamlit app that lets you interact with Google’s Gemini models using the `langchain-google-genai` integration.  
You can enter your own Gemini API key and start chatting instantly.

---

## 🚀 Features
- Clean and minimal UI powered by Streamlit  
- Secure sidebar input for your Gemini API Key  
- Uses LangChain to connect with Gemini models  
- Lightweight and quick to deploy on Streamlit Cloud or Hugging Face Spaces  

---

## 🛠️ Installation (Run Locally)

Clone the repository and install dependencies:

```bash
git clone https://github.com/HUDA-GIF/gemini-streamlit-chatbot.git
cd gemini-streamlit-chatbot
pip install -r requirements.txt
Run the app:

bash
Copy code
streamlit run streamlit_app.py
🌐 Deployment
This project is ready to be deployed on Hugging Face Spaces or Streamlit Cloud.
Just make sure requirements.txt and streamlit_app.py are in the root directory.

🔑 API Key
You’ll need a Gemini API key from Google to use this app.
Create one at 👉 Google AI Studio.

📂 Project Structure
Copy code
gemini-streamlit-chatbot/
 ├── streamlit_app.py
 ├── requirements.txt
 └── README.md
📖 About
A simple Streamlit app that lets users enter their own Google Gemini API key and chat with Gemini models (gemini-1.5-flash / gemini-1.5-pro) using LangChain.
