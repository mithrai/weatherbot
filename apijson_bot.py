import requests

print("Hello! (type 'exit' to stop):")

while True:
    user_input = input("You: ").lower()

    if user_input in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    if "joke" in user_input:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)

        if response.status_code == 200:
            joke = response.json()
            print(joke["setup"])
            print(joke["punchline"])
        else:
            print("Sorry, couldn't fetch a joke right now.")
    else:
        print("I can only tell jokes for now")
