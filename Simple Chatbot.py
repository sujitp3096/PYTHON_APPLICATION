while True:
    msg = input("You: ").lower()

    if msg == "hello":
        print("Bot: Hi!")
    elif msg == "how are you":
        print("Bot: I am fine.")
    elif msg == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")
