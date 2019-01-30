import requests, json

def weth(long, lat):
    long = input("What is the longitude")
    lat = input("What is the latitude")

    api_url = 'https://api.darksky.net/forecast/d8deca02a1eb45e5b8b90212736c5402/40.7128,74.0060'

    data = requests.get(api_url).json()
    return (data)

def variables(data):
    currently = weather ['currently']
    summary = currently ['summary']
    humiditiy = currently ['humidity']
    windSpeed = currently ['windSpeed']

    print(summary, humiditiy, windSpeed)
#d8deca02a1eb45e5b8b90212736c5402
    data = weather(40.7128, 74.0060)
variables(data)
