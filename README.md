# Weather_App


# Overview

Application that fetches real-time weather data and a 5-day forecast for any city using the OpenWeatherMap API. The app dynamically changes the background based on weather conditions.


# Features

- Fetch current weather details including temperature, condition, humidity, wind speed, and direction.

- Display sunrise and sunset times in UTC.

- Show a 5-day weather forecast.

- Dynamically update background images based on weather conditions.

- Simple and user-friendly interface.

- Built using Flask, HTML, CSS, and JavaScript.
- 

# Technologies Used

Python (Flask)

HTML, CSS, JavaScript

OpenWeatherMap API


# Installation

1. Clone the Repository

git clone https://github.com/your-username/weather-app.git
cd weather-app

2. Install Dependencies

Ensure you have Python installed, then install the required packages:

pip install flask requests

3. Get OpenWeatherMap API Key

Sign up at OpenWeatherMap and get your API key.

Replace API_KEY in app.py with your actual key:

API_KEY = "your_api_key_here"

4. Run the Application

python app.py

5. Open in Browser

Visit http://127.0.0.1:5000/ in your browser.


# Project Structure

weather-app/
│── static/
│   ├── sunny.webp
│   ├── cloudy.webp
│   ├── rainy.webp
│   ├── snow.webp
│   ├── mist.webp
│   ├── haze.webp
│   ├── fog.webp
│   ├── thunderstorm.webp
│── templates/
│   ├── index.html
│── app.py
│── README.md


# Usage

Open the app in your browser.

Enter a city name and click the Check Weather button.

View current weather details and a 5-day forecast.

The background will change based on the current weather conditions.


# API Reference

Current Weather API: http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric

Forecast API: http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric


# Contributing

Feel free to contribute by submitting issues or pull requests.

This is a Flask-based weather app
