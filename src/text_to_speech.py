from pyttsx3 import init


def text_to_speech(text: str) -> None:
    tts_engine = init()

    tts_engine.say(text)
    tts_engine.runAndWait()
