import streamlit as st
import speech_recognition as sr
import io
import wave

def voice_to_text(language="en-IN"):
    st.subheader("🎙 Speak now")

    audio = st.audio_input("Click and speak")

    if audio is None:
        return ""

    audio_bytes = audio.read()

    # WAV bytes read using wave module (built-in)
    with wave.open(io.BytesIO(audio_bytes), 'rb') as wf:
        sample_rate = wf.getframerate()
        frames = wf.readframes(wf.getnframes())

    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(
        frames,
        sample_rate=sample_rate,
        sample_width=2
    )

    try:
        text = recognizer.recognize_google(audio_data, language=language)
        return text
    except:
        return ""
