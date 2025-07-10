import streamlit as st
import requests
import re

st.set_page_config(page_title="WeatherBot", layout="centered")
st.title("WeatherBot - Real-Time Weather Info")

def extract_city(text):
    match = re.search(r'in ([a-zA-Z\s]+)', text.lower())
    if match:
        return match.group(1).strip().title()
    else:
        return text.strip().title()

user_input = st.text_input("Ask about the weather:")

if st.button("Check Weather"):
    if not user_input:
        st.warning("Please enter a city or natural question.")
    else:
        city = extract_city(user_input)

        url = f"https://wttr.in/{city}?format=j1"
        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                if "nearest_area" not in data or not data["nearest_area"][0]["areaName"][0]["value"]:
                    st.error("Unknown location. Please try again.")
                else:
                    current = data["current_condition"][0]
                    temperature = current["temp_C"]
                    feels_like = current["FeelsLikeC"]
                    condition = current["weatherDesc"][0]["value"]
                    humidity = current["humidity"]

                    area = data["nearest_area"][0]["areaName"][0]["value"]
                    country = data["nearest_area"][0]["country"][0]["value"]

                    st.subheader(f"Location: {area}, {country}")
                    st.markdown(f"""
                    **Temperature:** {temperature}°C  
                    **Feels Like:** {feels_like}°C  
                    **Condition:** {condition}  
                    **Humidity:** {humidity}%  
                    """)
            else:
                st.error("Could not fetch weather. Try again.")
        except Exception as e:
            st.error(f"Error occurred: {e}")
