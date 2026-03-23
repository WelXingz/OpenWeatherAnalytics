CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city TEXT,
    temperature FLOAT,
    humidity INT,
    weather TEXT,
    wind_speed FLOAT,
    collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);