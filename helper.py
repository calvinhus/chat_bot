import random
import requests
from datetime import datetime


def roll_dice():
    return f"You rolled a {str(random.randint(1, 6))}."


def rand_number():
    return f"{str(random.randint(0, 100))}"


def joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')

    return response.json()['value']


def weather():

    globalIdLocal = 1110600  # ID for Lisbon

    response = requests.get(
        f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{globalIdLocal}.json")

    weather_type = response.json()['data'][1]['idWeatherType']

    weather = requests.get(
        "https://api.ipma.pt/open-data/weather-type-classe.json")

    for w in weather.json()['data']:
        if w['idWeatherType'] == weather_type:
            return f"Weather for tomorrow: {w['descIdWeatherTypeEN']}"


def news(keyword):

    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey=b3a1f67e5db7436aa28ada511863cc6f"
    response = requests.get(url)
    news = response.json()['articles'][0]

    return f"{news['description']}<br><br>{news['url']}"


def math_facts():
    response = requests.get("http://numbersapi.com/random/math")
    return f"I love math!<br><br>Did you know that {response.text}"


def hour():
    now = datetime.now()
    return f"It's {str(now.hour)} hours and {str(now.minute)} minutes."
