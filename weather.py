from distutils.command.config import config
from urllib import response
from wsgiref.util import request_uri
import requests
import configparser

apikey = configparser.ConfigParser()
apikey.read("E:\Python\Weather fetcher\config.ini")

API_KEY = apikey.get('api', 'key')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("temperature:", temperature, "celcius")
else:
    print("An error occured.")