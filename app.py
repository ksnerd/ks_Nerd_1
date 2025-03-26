
import streamlit as st
import openai
import os

st.set_page_config(page_title="Pfarramtsleiter GPT", layout="centered")

st.title("Pfarramtsleiter-GPT")
st.write("Stelle deine Frage zu kirchlichen Regelungen und Gesetzen.")

user_input = st.text_input("Frage eingeben:")

if user_input:
    st.info("⏳ Die Antwort wird generiert...")
    try:
        openai.api_key = st.secrets["OPENAI_API_KEY"]
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "Du bist ein kirchlicher Assistent, der Fragen zu evangelischem Kirchenrecht beantwortet. Verwende Kirchengesetze der EVLKS, wenn möglich."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.3
        )
        answer = response["choices"][0]["message"]["content"]
        st.success(answer)
        st.markdown("---")
        st.markdown("**Beispielhafter Gesetzesauszug (Platzhalter):**

> § 4 KVwG: Der Kirchenvorstand ist beschlussfähig, wenn mehr als die Hälfte der Mitglieder anwesend ist.")
    except Exception as e:
        st.error("Fehler bei der Antwortgenerierung. Bitte API-Key prüfen oder später erneut versuchen.")

st.markdown("---")
st.markdown("**Hinweis:** Diese Antworten stellen keine rechtsverbindliche Auskunft dar. Bitte prüfen Sie alle Informationen eigenverantwortlich.  
**Projektleitung:** Sebastian Keller")
