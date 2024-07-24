import requests
option = "people"
url = f"https://swapi.dev/api/{option}/"
try: 
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    result = data["results"]
    print(f"Successfully retieved {len(result)} entities")
except requests.HTTPError as e:
    print(f"Failed to retrieve, error: {e}")
