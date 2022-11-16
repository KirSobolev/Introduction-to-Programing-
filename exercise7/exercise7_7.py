import json
import urllib.request
from datetime import datetime
from operator import itemgetter

url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
warnings = json.loads(raw_data)
counter = 0
cities_raw = [x['city'] for x in warnings]
slipperiest = 0
slipperiest_city = ""
latest = []
today = datetime.today()

for el in set(cities_raw):  # set(cities) consists of only city names without repeats
    if cities_raw.count(el) > slipperiest:  # Checks for the city with most entries
        slipperiest = cities_raw.count(el)
        slipperiest_city = el

warnings_sorted = sorted(warnings, key=itemgetter("updated_at"), reverse=True)  # Sorts dicts based on updated_at
print("The latest 5 slippery weather warnings are:")
for el in warnings_sorted[:4]:
    print(f"{el['city']} - {el['updated_at']}")
    # This actually prints last 5 warnings,
    # but atm they are all from Oulu, so here's part which prints 5 latest cities:

for el in warnings_sorted:
    if el["city"] not in latest and len(latest) < 5:
        latest.append(el["city"])

print(f"\nThe latest 5 cities with slippery weather warnings are: {', '.join(latest)}")

print(f"\nThe slipperiest city and absolute winner is {slipperiest_city} with {slipperiest} entries!")
