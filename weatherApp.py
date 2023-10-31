import requests
import os
from dotenv import load_dotenv
from pprint import pprint
import sys

load_dotenv()


def get_curr_weather(city):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\nGet current weather conditions")

    city = input("\nplease enter a city\n")

    if not bool(city.strip()):
        sys.exit("Bye..")

    weather_info = get_curr_weather(city)
    if not weather_info["cod"] == 200:
        sys.exit("Bye..")

    print("")

    pprint(weather_info)
