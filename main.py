import streamlit as st
from helper import get_weather

# App title and description
st.title("🌤️ Weather App")
st.subheader("Get real-time weather for any city")

# Input section
city = st.text_input("Enter a city name:", key="input")

# Fetch weather on button click
if st.button("Get Weather"):
    if city.strip():
        try:
            weather = get_weather(city)
            if isinstance(weather, dict):  # assuming dict response
                st.success(f"Weather in {city.title()}:")
                st.metric("🌡 Temperature", f"{weather.get('temp', 'N/A')} °C")
                st.write(f"**Condition:** {weather.get('description', 'N/A')}")
                st.write(f"**Humidity:** {weather.get('humidity', 'N/A')}%")
                st.write(f"**Wind Speed:** {weather.get('wind', 'N/A')} km/h")
            else:  # fallback if get_weather returns text
                st.info(weather)
        except Exception as e:
            st.error(f"Could not fetch weather: {e}")
    else:
        st.warning("Please enter a city name.")
