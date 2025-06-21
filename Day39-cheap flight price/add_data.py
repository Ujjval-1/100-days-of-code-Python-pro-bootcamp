import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

def add_city(from_city, to_city):
    url = SHEETY_ENDPOINT
    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}",
        "Content-Type": "application/json"
    }
    body = {
        "price": {
            "from": from_city,
            "fromIataCode": "",
            "to": to_city,
            "toIataCode": "",
            "lowestPrice": ""
        }
    }
    response = requests.post(url, json=body, headers=headers)
    if response.status_code in (200, 201):
        print(f"✅ Added route: {from_city} -> {to_city}")
    else:
        print(f"❌ Failed to add route: {from_city} -> {to_city} | Response: {response.text}")

if __name__ == "__main__":
    cities = [
        "Delhi",
        "Mumbai",
        "Chennai",
        "Kolkata",
        "Hyderabad",
        "Ahmedabad",
        "Pune",
        "Goa",
        "Jaipur",
        "Lucknow",
        "Cochin"
    ]

    # Remove Bangalore as per your request (if it was in the list)

    for origin_city in cities:
        for destination_city in cities:
            if origin_city != destination_city:
                add_city(origin_city, destination_city)
