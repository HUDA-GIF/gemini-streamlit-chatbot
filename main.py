import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("🦜🔗 Gemini Quickstart App")

gemini_api_key = st.sidebar.text_input("Gemini API Key", type="password")

def generate_response(input_text):
    llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # ✅ valid model
    google_api_key=gemini_api_key,
    temperature=0.7



    )
    response = llm.invoke(input_text)
    st.info(response.content)

with st.form("my_form"):
    text = st.text_area("Enter text:", "...")
    submitted = st.form_submit_button("Submit")

    if not gemini_api_key:
        st.warning("Please enter a valid Gemini API key!", icon="⚠")
    if submitted and gemini_api_key:
        generate_response(text)
