import requests
import psycopg2
import os
from datetime import datetime

API_KEY = os.environ.get("API_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")

CITY = "Curitiba"

# API
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Data Extraction
print(data)
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["description"]
wind_speed = data["wind"]["speed"]

# Database Connection
conn = psycopg2.connect(DATABASE_URL)

cursor = conn.cursor()

cursor.execute("""
    INSERT INTO weather_data (city, temperature, humidity, weather, wind_speed)
    VALUES (%s, %s, %s, %s, %s)
""", (CITY, temperature, humidity, weather, wind_speed))

conn.commit()
cursor.close()
conn.close()
