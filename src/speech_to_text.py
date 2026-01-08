import streamlit as st
import speech_recognition as sr
import io
import numpy as np
import soundfile as sf

def voice_to_text(language="en-IN"):
    st.subheader("🎙 Speak now")

    audio = st.audio_input("Click and speak")

    if audio is None:
        return ""

    # audio bytes read
    audio_bytes = audio.read()

    # bytes → numpy
    data, samplerate = sf.read(io.BytesIO(audio_bytes))

    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(
        data.tobytes(),
        samplerate=samplerate,
        sample_width=2
    )

    try:
        text = recognizer.recognize_google(audio_data, language=language)
        return text
    except:
        return ""
