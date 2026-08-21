import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good!", "Doing great!", "Awesome!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "how old are you": ["I'm 11", "I am 11 years old", "15"],
    "what is ai": ["AI stands for Artificial Intelligence.", "AI is a set of technologies that lets computers learn, solve problems, and make decisions like a human." ],
    "who are you": ["I'm Aisha", "Myself Aisha", "I am Aisha"]
}

print("Bot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower().strip()

    if user == "bye":
        print("Bot:", random.choice(responses["bye"]))
        break

    found = False

    for key in responses:
        if key in user or user in key:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("Bot: I don't know the answer to that.")

        teach = input("Would you like to teach me the answer? (yes/no): ").lower()

        if teach == "yes":
            answer = input("What should I answer? ")

            responses[user] = [answer]

            print("Bot: Thanks! I learned something new.")