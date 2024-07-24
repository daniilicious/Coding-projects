import requests

def fetch_data(option, count): #let's user decide which data is pulled
    
    url = f"https://swapi.dev/api/{option}/"
    result = []

    while len(result) < count:
        try: #handles http errors
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            result.extend(data["results"]) #extends result list
            print(f"Successfully retieved {len(result)} entities")
            url = data["next"] #next page of data
        except requests.HTTPError as e:
            print(f"Failed to retrieve, error: {e}")
        if not url:
            break

    if result: #displays star wars characters
        for person in result[:count]:
            print(person["name"])
        else:
            print("Unable to download data")
fetch_data("people", 10)
 