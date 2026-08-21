import random

import json


with open("response.json", "r") as file:
    response = json.load(file)

while True:
    user = input("You: ").lower()
    if user == "bye":
        print("Bot:", random.choice(responses["bye"]))
        break
    found = False

    for key in response:
        if key in user:
            print("Bot:", random.choice(response[key]))
            found = True
            break
            

    if not found:
        print("Bot: I don't understand that yet.")