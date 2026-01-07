import speech_recognition as sr

def voice_to_text(language="en-IN"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
