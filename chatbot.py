# Simple Chatbot Program
# Concepts used: Dictionary, if-else, while loop

print("🤖 Chatbot: Hello! Type 'bye' to exit.\n")

# Dictionary storing user inputs and bot responses
responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm doing great 😊",
    "what is your name": "I'm a simple chatbot 🤖",
    "who created you": "I was created using Python!",
    "thank you": "You're welcome 😊",
    "help": "I can answer simple questions like hi, hello, how are you, bye"
}

# Loop to keep chatbot running
while True:
    user_input = input("You: ").lower().strip()

    # Exit condition
    if user_input == "bye":
        print("Bot: Goodbye! Have a nice day 😊")
        break

    # Check predefined responses
    elif user_input in responses:
        print("Bot:", responses[user_input])

    # Default response
    else:
        print("Bot: Sorry, I don't understand that 🤔")
