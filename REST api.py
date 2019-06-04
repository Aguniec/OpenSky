import requests
import json


resposne = requests.get(
    "https://opensky-network.org/api/states/all")
#    "https://opensky-network.org/api/states/all?icao24")
data = resposne.json()
# print(resposne.json())
for item in data["states"]:
    print("callsign of airplane : {}, origin_country : {}".format(
        item[1], item[2]))
