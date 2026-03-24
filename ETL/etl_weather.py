import requests
import psycopg2
import os
from datetime import datetime

API_KEY = os.environ.get("API_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")

capitals = [
    "Curitiba",
    "Sao Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Brasilia",
    "Salvador",
    "Fortaleza",
    "Recife",
    "Porto Alegre",
    "Manaus",
    "Belem",
    "Goiania",
    "Florianopolis",
    "Vitoria",
    "Natal",
    "Joao Pessoa",
    "Maceio",
    "Aracaju",
    "Cuiaba",
    "Campo Grande",
    "Palmas",
    "Boa Vista",
    "Rio Branco",
    "Macapa",
    "Porto Velho",
    "Teresina",
    "Sao Luis"
]

# connection
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

for city in capitals:
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},BR&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        data = response.json()

        if "main" not in data:
            print(f"City error {city}: {data}")
            continue

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        #INSERT 
        cursor.execute("""
            INSERT INTO weather_data (city, temperature, humidity, weather, wind_speed)
            VALUES (%s, %s, %s, %s, %s)
        """, (city, temperature, humidity, weather, wind_speed))

        print(f"{city} inserted")

    except Exception as e:
        print(f"Major error in {city}: {e}")
        continue

#commit
conn.commit()

cursor.close()
conn.close()