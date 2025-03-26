import streamlit as st
import openai

st.set_page_config(page_title="Pfarramtsleiter GPT", layout="centered")

st.title("Pfarramtsleiter-GPT – API-Test")
st.write("Wir testen, ob die Verbindung zur OpenAI-API funktioniert.")

try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    models = openai.Model.list()
    st.success("✅ Verbindung zur OpenAI-API erfolgreich!")
except Exception as e:
    st.error(f"❌ Fehler beim API-Zugriff:\n\n{e}")
