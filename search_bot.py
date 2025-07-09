import json

with open("people_data.json", "r") as file:
    people = json.load(file)

print("Hello! Ask me about someone (type 'exit' to quit):")

while True:
    name = input("Enter a name: ").lower()

    if name in ['exit', 'quit']:
        print("Goodbye!")
        break

    found = False
    for person in people:
        if person["name"].lower() == name:
            print(f"{person['name']} is {person['age']} years old and lives in {person['city']}")
            found = True
            break

    if not found:
        print("Sorry, I couldn't find that person.")
