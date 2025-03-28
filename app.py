
import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="Pfarramtsleiter GPT", layout="centered")

st.title("Pfarramtsleiter-GPT")
st.write("Stelle deine Frage zu kirchlichen Regelungen und Gesetzen.")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

user_input = st.text_input("Frage eingeben:")

if user_input:
    st.info("⏳ Die Antwort wird generiert...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Du bist ein kirchlicher Assistent, der Fragen zu evangelischem Kirchenrecht beantwortet. Verwende Kirchengesetze der EVLKS, wenn möglich. Du findest Kirchengesetze auf www.evlks.de und unterseiten. Gib die Quellen als Links in deiner Antwort an!"},
                {"role": "user", "content": user_input},
            ],
            temperature=0.3
        )
        answer = response.choices[0].message.content
        st.success(answer)
        st.markdown("---")
        st.markdown("**Beispielhafter Gesetzesauszug (Platzhalter):**\n\n> § 4 KVwG: Der Kirchenvorstand ist beschlussfähig, wenn mehr als die Hälfte der Mitglieder anwesend ist.")
    except Exception as e:
        st.error(f"Fehler bei der Antwortgenerierung:\n\n{e}")
assistant_id = "asst_abc123xyz"
thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_input
)
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant_id
)

# Optional: auf das Ergebnis warten (Polling)
result = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)


st.markdown("---")
st.markdown("**Hinweis:** Diese Antworten stellen keine rechtsverbindliche Auskunft dar. Bitte prüfen Sie alle Informationen eigenverantwortlich.  \n**Projektleitung:** Sebastian Keller")
