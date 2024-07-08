from constants import EXIT_COMMANDS, GOODBYE_MSG, HELLO_MSG, LISTENING_MSG
from get_response import get_response
from print_message import print_message
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech

if __name__ == "__main__":
    print_message(HELLO_MSG, "assistant")
    text_to_speech(HELLO_MSG)

    running = True

    while running:
        print_message(LISTENING_MSG, "assistant")

        user_input = speech_to_text()
        print_message(user_input.capitalize(), "user")

        # Quit scenario
        if user_input.lower() in EXIT_COMMANDS:
            print_message(GOODBYE_MSG, "assistant")
            text_to_speech(GOODBYE_MSG)

            running = False
            break

        reply = get_response(user_input)

        print_message(reply, "assistant")
        text_to_speech(reply)
