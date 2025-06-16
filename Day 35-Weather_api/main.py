import requests

parameter = {
    "lat":24.311991,
    "lon":76.216759,
    "appid":"89047385ffe62f21d429a641369ddff5",
    "cnt":4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameter)

response.raise_for_status()
data=response.json()
print(data)