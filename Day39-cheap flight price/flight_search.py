import requests
from datetime import datetime, timedelta

class FlightSearch:
    def __init__(self, token):
        self.token = token
        self.url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    def search(self, origin, destination):
        headers = {"Authorization": f"Bearer {self.token}"}
        departure_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        return_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "currencyCode": "INR",
            "max": 1
        }
        response = requests.get(self.url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get("data"):
            return data["data"][0]["price"]["total"]
        return None
