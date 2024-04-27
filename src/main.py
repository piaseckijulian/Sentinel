import os

import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)
messages = [
    {
        "role": "system",
        "content": "You are a personal assistant called Sentinel. Act like you are a personal assistant. Your goal is to help me with tasks.",
    }
]


def text_to_speech(text):
    tts_engine = pyttsx3.init()
    voices = tts_engine.getProperty("voices")
    tts_engine.setProperty("voice", voices[1].id)
    tts_engine.say(text)
    tts_engine.runAndWait()


def listen_for_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sentinel: Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio).strip()
        print(f"You: {user_input}")
        return user_input
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return f"Error: {str(e)}"


def get_response(prompt):
    try:
        messages.append({"role": "user", "content": prompt})

        res = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        reply = res.choices[0].message

        messages.append({"role": "assistant", "content": reply.content})

        return reply.content
    except Exception as e:
        return str(e)


def main():
    print("Sentinel: Hello! How can I assist you today?")
    text_to_speech("Hello! How can I assist you today?")
    running = True
    while running:
        user_input = listen_for_voice()
        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
            print("Sentinel: Goodbye!")
            text_to_speech("Goodbye")
            running = False
            break

        response = get_response(user_input)
        print(f"Sentinel: {response}")
        text_to_speech(response)


main()
