# app.py
from src.speech_to_text import voice_to_text
from src.predict_emotion import predict_emotion

def main():
    print("🎧 Voice Emotion Detection Started")

    text = voice_to_text()

    if text == "":
        print("❌ Please Try Again")
        return

    emotion = predict_emotion(text)

    print(" Detected Emotion:", emotion)

if __name__ == "__main__":
    main()
