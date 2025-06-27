def simple_chatbot():
    print("🤖 Hello! I’m ChatBot. Type 'bye' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print("Bot: Hi there!")
        elif "how are you" in user_input:
            print("Bot: I'm just a bunch of code, but I'm doing great! How about you?")
        elif "what's your name" in user_input:
            print("Bot: I'm CodeAlpha Bot!")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day 😊")
            break
        else:
            print("Bot: Sorry, I don’t understand that.")

if __name__ == "__main__":
    simple_chatbot()