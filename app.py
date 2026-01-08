import streamlit as st
from src.speech_to_text import voice_to_text
from src.emotion_model import predict_emotion   # tumhara model

st.title("🎧 Voice Emotion Detection")

text = voice_to_text()

if text != "":
    st.write("📝 Recognized Text:", text)
    emotion = predict_emotion(text)
    st.success(f"😊 Emotion: {emotion}")
else:
    st.info("Please speak to detect emotion")
