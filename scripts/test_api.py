import requests

url = "https://lldev.thespacedevs.com/2.2.0/launch/upcoming/"

response = requests.get(url)

print("Status:", response.status_code)

data = response.json()

print("Esimene start:")
print(data["results"][0]["name"])
