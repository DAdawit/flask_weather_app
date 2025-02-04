from dotenv import load_dotenv
from pprint import pprint
import requests
import os
load_dotenv()

def get_current_weather(city):
        request_url  = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY_WEATHER")}&q={city}&units=metric'
        response = requests.get(request_url).json()
        return response

if __name__ == "__main__":
    print('\n*** Get current weather Contitions ***\n')
    city = input(f"Please enter a city name: ")
    weather_data = get_current_weather(city)
    print(f'\nCurrent weather for {weather_data["name"]}:')
    print(f'\nThe temp is {weather_data["main"]["temp"]:.1f}°')
    print(f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')
    
