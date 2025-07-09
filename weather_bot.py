import requests

while True:
    city = input("City Name: ").strip()

    if city == "exit":
        print("Goodbye!")
        break

    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        current = data["current_condition"][0]
        temperature = current["temp_C"]
        weather_desc = current["weatherDesc"][0]["value"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]

        print(f"\n Weather in {city.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Condition: {weather_desc}")
        print(f"Humidity: {humidity}%\n")

    else:
        print("Could not fetch weather. Try again.")



