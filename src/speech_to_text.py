from speech_recognition import Microphone, Recognizer, UnknownValueError

from constants import FALLBACK_MSG
from text_to_speech import text_to_speech


def speech_to_text() -> str:
    recognizer = Recognizer()

    with Microphone() as src:
        recognizer.adjust_for_ambient_noise(src)
        audio = recognizer.listen(src)

    try:
        user_input: str = recognizer.recognize_google(audio).strip()

        return user_input
    except UnknownValueError:
        text_to_speech(FALLBACK_MSG)

        return FALLBACK_MSG
    except Exception as e:
        return f"Something went wrong! Error: {str(e)}"
