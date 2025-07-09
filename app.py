import streamlit as st
import requests

st.set_page_config(page_title="WeatherBot")
st.title("WeatherBot - Real-Time Weather Information")

city = st.text_input("Enter a city name:")

if city:
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            if "nearest_area" not in data or not data["nearest_area"][0]["areaName"][0]["value"]:
                st.error("Unknown location. Please enter a valid city.")

            else:
                current = data["current_condition"][0]
                temperature = current["temp_C"]
                feels_like = current["FeelsLikeC"]
                condition = current["weatherDesc"][0]["value"]
                humidity = current["humidity"]

                area = data["nearest_area"][0]["areaName"][0]["value"]
                country = data["nearest_area"][0]["country"][0]["value"]
                st.write(f"Location matched: {area}, {country}")
            
                st.subheader(f"Weather in {city.title()}")
                st.markdown(f"""
                Temperature: {temperature}°C  
                Feels Like: {feels_like}°C  
                Condition: {condition}  
                Humidity: {humidity}%  
                """)
        else:
            st.error("Could not fetch weather. Please try again.")
    except Exception as e:
        st.error(f"Error: {e}")
