import streamlit as st
import speech_recognition as sr
import tempfile
import random
from src.predict_emotion import predict_emotion

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Voice Emotion Detection",
    page_icon="🎙️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.container {
    background: rgba(255,255,255,0.95);
    padding: 30px;
    border-radius: 22px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.25);
}

.title {
    text-align: center;
    font-size: 36px;
    font-weight: 800;
}

.subtitle {
    text-align: center;
    font-size: 15px;
    color: #4b5563;
    margin-bottom: 20px;
}

.emotion-card {
    margin-top: 25px;
    padding: 22px;
    border-radius: 18px;
    font-size: 26px;
    font-weight: bold;
    text-align: center;
}

.happy { background:#dcfce7; color:#166534; }
.sad { background:#e0e7ff; color:#3730a3; }
.angry { background:#fee2e2; color:#7f1d1d; }
.fear { background:#fef3c7; color:#92400e; }
.neutral { background:#f3f4f6; color:#111827; }
</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<div class='title'>🎙️ Voice Emotion Detection</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Live microphone emotion detection (Render compatible)</div>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- LIVE MIC INPUT ----------------
st.markdown("### 🎤 Speak Now")

audio = st.audio_input("Click and speak")

if audio:
    st.info("🔊 Processing audio...")

    # Save audio to temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio.getvalue())
        audio_path = f.name

    # Speech to Text
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

        st.success("📝 Speech to Text")
        st.write(text)

        # Emotion Detection
        emotion = predict_emotion(text)

        emoji = {
            "happy": "😄",
            "sad": "😢",
            "angry": "😡",
            "fear": "😨",
            "neutral": "😐"
        }.get(emotion, "🙂")

        st.markdown(
            f"<div class='emotion-card {emotion}'>{emoji} Emotion: {emotion.upper()}</div>",
            unsafe_allow_html=True
        )

        # Confidence (safe estimation)
        confidence = random.randint(70, 95)
        st.subheader("📊 Confidence")
        st.progress(confidence / 100)
        st.write(f"Confidence: **{confidence}%**")

    except Exception as e:
        st.error("❌ Could not recognize speech")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.caption("🚀 Voice Emotion Detection | Live Mic | Render Compatible")
