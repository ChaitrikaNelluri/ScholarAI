import speech_recognition as sr
from gtts import gTTS
import tempfile
import os
import streamlit as st


def speech_to_text():

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            st.info("🎤 Listening...")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)

        return text

    except Exception:

        st.error("Couldn't recognize your voice.")

        return ""


def text_to_speech(text):

    tts = gTTS(text=text, lang="en")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:

        filename = fp.name

    tts.save(filename)

    audio_file = open(filename, "rb")

    st.audio(audio_file.read(), format="audio/mp3")

    audio_file.close()

    os.remove(filename)