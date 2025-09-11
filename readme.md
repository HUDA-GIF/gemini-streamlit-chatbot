title: Gemini Streamlit Chatbot
emoji: 🦜
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.38.0"
app_file: streamlit_app.py
pinned: false

# Gemini Streamlit Chatbot

This is a simple chatbot built with **Streamlit** and **Google Gemini** using `langchain_google_genai`.  
Enter your Gemini API key in the sidebar and chat with the model!

# 🦜🔗 Gemini Quickstart App

This is a simple Streamlit app that lets you interact with **Google’s Gemini models** using the `langchain-google-genai` integration.  
You can enter your own Gemini API key and start chatting instantly.

## 🚀 Features
- Clean and minimal UI powered by **Streamlit**
- Secure sidebar input for your **Gemini API Key**
- Uses **LangChain** to connect with Gemini models
- Lightweight and quick to deploy on **Streamlit Cloud**

## 🛠️ Installation (Run Locally)
Clone the repository and install dependencies:
```bash
git clone https://github.com/HUDA-GIF/gemini-streamlit-chatbot.git
cd gemini-streamlit-chatbot
pip install -r requirements.txt
Run the app:

bash
Copy code
streamlit run main.py
🌐 Deployment
This project is ready to be deployed on Streamlit Cloud.
Just connect your GitHub repo, select main.py as the entry point, and deploy.

🔑 API Key
You’ll need a Gemini API key from Google to use this app.
You can create one at: Google AI Studio.

📂 Project Structure
css
Copy code
gemini-streamlit-chatbot/
 ├── main.py
 ├── requirements.txt
 └── README.md