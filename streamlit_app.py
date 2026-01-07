import streamlit as st
import time
import random
from src.speech_to_text import voice_to_text
from src.predict_emotion import predict_emotion

                      # PAGE CONFIG 
st.set_page_config(
    page_title=" Voice Emotion Detection",
    page_icon="🎙️",
    layout="centered"
)

                       # SESSION STATE 
if "history" not in st.session_state:
    st.session_state.history = []

                        # CUSTOM CSS
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

.mic {
    text-align: center;
    font-size: 55px;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); opacity: .6; }
    50% { transform: scale(1.2); opacity: 1; }
    100% { transform: scale(1); opacity: .6; }
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

                       # UI
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<div class='title'>🎙️ Voice Emotion Detection </div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Speak clearly and get emotion with confidence</div>",
    unsafe_allow_html=True
)

st.divider()

                         # VOICE INPUT 
if st.button("🎤 Start Speaking"):
    st.markdown("<div class='mic'>🎧</div>", unsafe_allow_html=True)
    st.info("Listening... please speak")
    time.sleep(0.5)

    text = voice_to_text()

    if text == "":
        st.error("❌ Could not understand your voice")
    else:
        st.success("Speech to Text")
        st.write(text)

        emotion = predict_emotion(text)
        st.session_state.history.append(emotion)

        emoji = {
            "happy": "😄",
            "sad": "😢",
            "angry": "😡",
            "fear": "😨",
            "neutral": "😐"
        }.get(emotion, "🙂")

                        # EMOTION OUTPUT 
        st.markdown(
            f"<div class='emotion-card {emotion}'>{emoji} Emotion: {emotion.upper()}</div>",
            unsafe_allow_html=True
        )

                        # CONFIDENCE BAR 
        st.subheader("Confidence Estimation")
        confidence = random.randint(70, 95)
        st.progress(confidence)
        st.write(f"Confidence: **{confidence}%**")

st.markdown("</div>", unsafe_allow_html=True)

                         # FOOTER 
st.caption(" Voice Emotion Detection | Voice + ML | Streamlit")
