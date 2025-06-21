import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.sheety_url = os.getenv("SHEETY_ENDPOINT")
        self.sheety_token = os.getenv("SHEETY_TOKEN")
        self.amadeus_api_key = os.getenv("AMADEUS_API_KEY")
        self.amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
        self.amadeus_token = None

    def get_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": self.amadeus_api_key,
            "client_secret": self.amadeus_api_secret
        }
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            print("❌ Token error:", response.text)
        response.raise_for_status()
        self.amadeus_token = response.json()["access_token"]
        return self.amadeus_token

    def fetch_cities(self):
        headers = {"Authorization": f"Bearer {self.sheety_token}"}
        response = requests.get(self.sheety_url, headers=headers)
        response.raise_for_status()
        return response.json().get("prices", [])

    def get_iata_code(self, city_name):
        url = "https://test.api.amadeus.com/v1/reference-data/locations"
        headers = {"Authorization": f"Bearer {self.amadeus_token}"}
        params = {
            "keyword": city_name,
            "subType": "CITY"
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json().get("data")
        if data:
            return data[0]["iataCode"]
        return None

    def update_iata_code(self, city_id, iata_code, is_from=True):
        url = f"{self.sheety_url}/{city_id}"
        headers = {
            "Authorization": f"Bearer {self.sheety_token}",
            "Content-Type": "application/json"
        }
        key = "fromIataCode" if is_from else "toIataCode"
        body = {
            "price": {
                key: iata_code
            }
        }
        response = requests.put(url, json=body, headers=headers)
        response.raise_for_status()

    def update_price(self, city_id, price):
        url = f"{self.sheety_url}/{city_id}"
        headers = {
            "Authorization": f"Bearer {self.sheety_token}",
            "Content-Type": "application/json"
        }
        body = {
            "price": {
                "lowestPrice": price
            }
        }
        response = requests.put(url, json=body, headers=headers)
        response.raise_for_status()
