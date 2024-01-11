import requests
import json
import os

def geocode(address, api_key):
    """Fonction pour géocoder une adresse en utilisant l'API Google Maps."""
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    api_key = os.environ["API"]
    address = "Webitech, FRANCE"

    result = geocode(address, api_key)
    if result:
        print(json.dumps(result, indent=4))
    else:
        print("Erreur lors du géocodage de l'adresse.")

if __name__ == "__main__":
    main()
