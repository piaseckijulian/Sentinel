from os import getenv

from dotenv import load_dotenv
from openai import OpenAI

from constants import SYSTEM_INITIAL_MSG

load_dotenv()

OPENAI_API_KEY = getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)
messages = [SYSTEM_INITIAL_MSG]


def get_reply(prompt: str) -> str:
    try:
        messages.append({"role": "user", "content": prompt})

        res = client.chat.completions.create(messages=messages, model="gpt-4o")
        reply = res.choices[0].message

        messages.append({"role": "assistant", "content": reply.content})

        return reply.content
    except Exception as e:
        return f"Something went wrong! Error: {str(e)}"
