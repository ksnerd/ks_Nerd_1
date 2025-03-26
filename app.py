
import streamlit as st
import openai

st.set_page_config(page_title="Pfarramtsleiter GPT", layout="centered")

st.title("Pfarramtsleiter-GPT")
st.write("Stelle deine Frage zu kirchlichen Regelungen und Gesetzen.")

user_input = st.text_input("Frage eingeben:")

if user_input:
    st.info("⏳ Die Antwort wird generiert...")
            openai.api_key = st.secrets["OPENAI_API_KEY"]
        try:
            models = openai.Model.list()
            st.success("✅ Verbindung zur OpenAI-API erfolgreich!")
        except Exception as inner_error:
            st.error(f"❌ Fehler beim API-Zugriff: {inner_error}")

    except Exception as e:
        st.error("Fehler bei der Antwortgenerierung. Bitte API-Key prüfen oder später erneut versuchen.")

st.markdown("---")
st.markdown("**Hinweis:** Diese Antworten stellen keine rechtsverbindliche Auskunft dar. Bitte prüfen Sie alle Informationen eigenverantwortlich.  \n**Projektleitung:** Sebastian Keller")
