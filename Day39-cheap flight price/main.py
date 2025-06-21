from data_manager import DataManager
from flight_search import FlightSearch

def select_city(cities, prompt):
    print(prompt)
    for idx, city in enumerate(cities, 1):
        print(f"{idx}. {city['from']} -> {city['to']}")
    while True:
        choice = input("Enter number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(cities):
            return cities[int(choice) - 1]
        print("Invalid choice, try again.")

def main():
    try:
        data_manager = DataManager()
        token = data_manager.get_token()
        flight_search = FlightSearch(token)

        cities = data_manager.fetch_cities()
        if not cities:
            print("⚠️ No routes found in Sheety.")
            return

        # Ensure all routes have IATA codes filled
        for route in cities:
            if not route.get("fromIataCode"):
                iata_from = data_manager.get_iata_code(route["from"])
                if iata_from:
                    data_manager.update_iata_code(route["id"], iata_from, is_from=True)
                    route["fromIataCode"] = iata_from
            if not route.get("toIataCode"):
                iata_to = data_manager.get_iata_code(route["to"])
                if iata_to:
                    data_manager.update_iata_code(route["id"], iata_to, is_from=False)
                    route["toIataCode"] = iata_to

        print("\nSelect route to search flights:")
        selected_route = select_city(cities, "Choose your route:")
        print(f"✅ Selected: {selected_route['from']} ({selected_route['fromIataCode']}) -> {selected_route['to']} ({selected_route['toIataCode']})")

        if selected_route['fromIataCode'] == selected_route['toIataCode']:
            print("⚠️ Origin and destination cannot be the same.")
            return

        print("\n🔎 Searching flight...")
        price = flight_search.search(selected_route['fromIataCode'], selected_route['toIataCode'])
        if price:
            print(f"✅ Lowest price from {selected_route['fromIataCode']} to {selected_route['toIataCode']}: ₹{price}")
            data_manager.update_price(selected_route["id"], price)
            print("✅ Price updated in Sheety.")
        else:
            print("⚠️ No flights found.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
