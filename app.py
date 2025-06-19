import gradio as gr
import requests

API_KEY = "34d80e0093744809bd2161247251906"

def get_weather(city):
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city},India"
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            return f"❌ Error: {data['error']['message']}"

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        return (
            f"📍 Location: {location}, {country}\n"
            f"🌤️ Condition: {condition}\n"
            f"🌡️ Temperature: {temp_c}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind: {wind} km/h"
        )

    except Exception as e:
        return f"❌ Exception: {str(e)}"

cities = [
    "Amaravati", "Itanagar", "Dispur", "Patna", "Raipur", "Panaji", "Gandhinagar", "Chandigarh",
    "Shimla", "Ranchi", "Bengaluru", "Thiruvananthapuram", "Bhopal", "Mumbai", "Imphal", "Shillong",
    "Aizawl", "Kohima", "Bhubaneswar", "Jaipur", "Gangtok", "Chennai", "Hyderabad", "Agartala",
    "Lucknow", "Dehradun", "Kolkata", "Delhi", "Puducherry", "Port Blair", "Daman", "Kavaratti",
    "Leh", "Srinagar", "Silvassa"
]

demo = gr.Interface(
    fn=get_weather,
    inputs=gr.Dropdown(choices=cities, label="Select a city"),
    outputs=gr.Textbox(label="Weather Info"),
    title="🌦️ Weather Bot (Powered by WeatherAPI.com)",
    description="Select an Indian city to get current weather details"
)

demo.launch(share=True)
