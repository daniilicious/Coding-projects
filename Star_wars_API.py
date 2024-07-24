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
            url = data["next"] #next page of data
        except requests.HTTPError as e:
            return None
        
        if url is None:
            break
    return result[:count]

count = int(input("Number of entities to download: "))
result = fetch_data("people", count) #function call

if result: #displays star wars characters
     for entity in result:
        print(entity["name"])
else:
    print("Unable to download data") 

