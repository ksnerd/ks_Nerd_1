
import streamlit as st

st.set_page_config(page_title="Pfarramtsleiter GPT", layout="centered")

st.title("Pfarramtsleiter-GPT")
st.write("Stelle deine Frage zu kirchlichen Regelungen und Gesetzen.")

user_input = st.text_input("Frage eingeben:")

if user_input:
    st.write("⏳ Die Antwort wird gesucht...")
    # Platzhalter für echte Antwortlogik
    st.success("Beispielantwort: Die Kirchenvorstandssitzung ist beschlussfähig, wenn mehr als die Hälfte der Mitglieder anwesend ist.")
