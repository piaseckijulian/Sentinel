from typing import Literal

Role = Literal["user", "assistant"]


def print_message(text: str, role: Role) -> None:
    if role == "user":
        speaker = "You"
    elif role == "assistant":
        speaker = "Sentinel"

    print(f"{speaker}: {text}")
