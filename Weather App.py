from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "683a593d447345d2a2b432b25c5309f1"

WEATHER_ICONS = {
    "Clear": "sunny.webp",
    "Clouds": "cloudy.webp",
    "Rain": "rainy.webp",
    "Snow": "snow.webp",
    "Mist": "mist.webp",
    "Haze": "haze.webp",
    "Fog": "fog.webp",
    "Thunderstorm": "thunderstorm.webp",
}

@app.route('/')
def home():
    city = request.args.get('city', 'Bengaluru')  # Default city
    current_weather, forecast = get_weather(city)

    if current_weather and forecast:
        bg_image = WEATHER_ICONS.get(current_weather["condition"], "sunny.webp")

        return render_template(
            "index.html",
            city=city,
            bg_image=bg_image,
            current=current_weather,
            forecast=forecast
        )
    
    return render_template("index.html", city=None)

def get_weather(city):
    # Current Weather Data
    url_now = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response_now = requests.get(url_now)

    # Forecast Data (Next 5 Days)
    url_forecast = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response_forecast = requests.get(url_forecast)

    if response_now.status_code == 200 and response_forecast.status_code == 200:
        data_now = response_now.json()
        data_forecast = response_forecast.json()

        # Extracting current weather details
        sunrise_time = datetime.utcfromtimestamp(data_now["sys"]["sunrise"]).strftime('%H:%M:%S')
        sunset_time = datetime.utcfromtimestamp(data_now["sys"]["sunset"]).strftime('%H:%M:%S')
        
        current_weather = {
            "temperature": data_now["main"]["temp"],
            "condition": data_now["weather"][0]["main"],
            "humidity": data_now["main"]["humidity"],
            "wind_speed": data_now["wind"]["speed"],
            "wind_direction": data_now["wind"]["deg"],
            "sunrise": sunrise_time,
            "sunset": sunset_time
        }

        # Extracting 5-day forecast
        forecast_list = []
        for item in data_forecast["list"][::8]:  # Get data at 24-hour intervals
            forecast_list.append({
                "date": item["dt_txt"].split()[0],
                "temp": item["main"]["temp"],
                "condition": item["weather"][0]["main"],
                "humidity": item["main"]["humidity"],
                "wind_speed": item["wind"]["speed"]
            })

        return current_weather, forecast_list

    return None, None

if __name__ == "__main__":
    app.run(debug=True)
