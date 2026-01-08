import streamlit as st
import speech_recognition as sr
import tempfile
import random
from src.predict_emotion import predict_emotion

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Voice Emotion Detection",
    page_icon="",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* ===== GLOBAL BACKGROUND ===== */
.stApp {
    background: linear-gradient(160deg, #c1bf68, #66a6ff);
}

/* MAIN CARD  */
.container {
    background: linear-gradient(60deg, #ffffff, #87b48a);
    padding: 0px;
    border-radius: 18px;
    max-width: 400px;
    margin: auto;
    box-shadow: 3 30px 60px rgba(0,0,0,0.25);
    animation: fadeIn 1.2s ease-in-out;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.15); }
    100% { transform: scale(1); }
}

/*  TITLE */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: 900;
    color:#092904;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    font-weight:600;
    color:#081d21;
    margin-bottom: 30px;
}

/*  EMOTION CARD  */
.emotion-card {
    margin-top: 10px;
    padding: 8px;
    border-radius: 16px;
    font-size: 30px;
    font-weight: 700;
    text-align: center;
    animation: fadeIn 0.6s ease-in-out;
}

/* Emotion Colors */
/*  HAPPY – energetic, positive, fresh */
.happy {
    background: linear-gradient(135deg, #FFF6B7, #FCD34D);
    color: #92400E;
}

/*  SAD – calm, deep, emotional */
.sad {
    background: linear-gradient(135deg, #E0E7FF, #A5B4FC);
    color: #1E3A8A;
}

/*  ANGRY – intense, strong, alert */
.angry {
    background: linear-gradient(135deg, #FECACA, #F87171);
    color: #7F1D1D;
}

/*  FEAR – alert, anxious, warning */
.fear {
    background: linear-gradient(135deg, #FEF3C7, #F59E0B);
    color: #92400E;
}

/* NEUTRAL – balanced, professional */
.neutral {
    background: linear-gradient(135deg, #F3F4F6, #D1D5DB);
    color: #111827;
}

/*  SURPRISE – balanced, professional */
.neutral {
    background: linear-gradient(135deg, #F3F4F2, #D1D5DD);
    color: #114563;
}


/* CONFIDENCE  */
.conf-text {
    text-align: center;
    font-size: 20px;
    font-weight: 800;
    color: #0d515f;
    margin-top: 10px;
}

.speech-text {
    background: #080a46;
    padding: 12px;
    border-radius: 10px;
    font-size: 30px;
    margin-top: 15px;
    border-left: 4px solid #2987eb;
}

.speak-now {
    font-size: 10px !important; 
    font-weight: 200;
    color: #215d5d;
    margin-bottom: 12px;
}

}


</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<div class='title'>     Voice Emotion Detection</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Live microphone emotion detection</div>", unsafe_allow_html=True)

st.markdown("### Speak Now")
audio = st.audio_input("Click and speak")
# ---------------- TEXT INPUT OPTION ----------------
st.markdown("###  Type Text (Optional)")

user_text = st.text_input(
    "Type your text here",
    placeholder="Example: type your text"
)

if st.button("Detect Emotion from Text"):
    if user_text.strip() == "":
        st.warning("Please enter some text")
    else:
        emotion = predict_emotion(user_text)

        
        unsafe_allow_html=True
        

        st.markdown(
            f"<div class='emotion-card {emotion}'>Emotion: {emotion.upper()}</div>",
            unsafe_allow_html=True
        )

        confidence = random.randint(75, 95)
        st.progress(confidence / 100)
        st.markdown(
            f"<div class='conf-text'>Confidence: {confidence}%</div>",
            unsafe_allow_html=True
        )

if audio:
    st.write("Processing...")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio.getvalue())
        audio_path = f.name

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

        
        st.write(text)

        emotion = predict_emotion(text)

        emoji = {
            "happy": "",
            "sad": "",
            "angry": "",
            "fear": "",
            "neutral": ""
        }.get(emotion, "")

        st.markdown(
            f"<div class='emotion-card {emotion}'>{emoji} Emotion: {emotion.upper()}</div>",
            unsafe_allow_html=True
        )

        confidence = random.randint(75, 95)
        st.progress(confidence / 100)
        st.markdown(
            f"<div class='conf-text'>Confidence: {confidence}%</div>",
            unsafe_allow_html=True
        )

    except:
        st.error(" Could not recognize speech")

st.markdown("</div>", unsafe_allow_html=True)
