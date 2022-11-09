import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)
weakest_wind = 0
strongest_wind = 0
weakest_wind_city = ""
strongest_wind_city = ""
avg_winds = {"lapland": [],
             "middle": [],
             "south": []}

for element in weather:
    if element["wind"] < weakest_wind or weakest_wind == 0:  # Searches for the weakest wind
        weakest_wind = element["wind"]
        weakest_wind_city = element["location"]
    elif element["wind"] > strongest_wind:  # Searches for the strongest wind
        strongest_wind = element["wind"]
        strongest_wind_city = element["location"]
    avg_winds[element["area"]].append(element["wind"])  # Adds wind value to the list in the dictionary based on area

for k, v in avg_winds.items():  # Counts average value of each list in dictionary
    new_value = round(sum(v) / len(v), 1)
    avg_winds[k] = new_value

print(f"Strongest wind today at location : {strongest_wind_city}, {strongest_wind} m/s")
print(f"Weakest wind today at location: {weakest_wind_city}, {weakest_wind} m/s \n")
for key, value in avg_winds.items():
    # Most probably next if statements are hardcoded and unnecessary but can't find a better solution atm
    if key == "middle":
        key = "middle part of Finland"
    elif key == "south":
        key = "southern Finland"
    print(f"Average wind, {key.capitalize()}: {value} m/s")
