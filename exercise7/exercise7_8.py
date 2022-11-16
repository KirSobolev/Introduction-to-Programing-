import json
import urllib.request

url = "https://api.ouka.fi/v1/chc_waiting_times_monthly_stats?order=year.desc,month.desc"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
data = json.loads(raw_data)
data_processed = []
queues = []
check = True

while check:
    try:
        year_input = int(input("What is the year you are interested of? (2017 - 2021)"))
        if year_input not in range(2017, 2022):
            raise ValueError
        check = False
    except ValueError:
        print("Wrong year!Try again!")

for el in data:
    if el["doctor_queue"] is None or el["nurse_queue"] is None or el["time"] is None or el["year"] is None \
            or el["month"] is None or el["day"] is None:
        # Here I've decided to exclude data with "queue = null", because it would ruin dataset as well
        continue
    else:
        data_processed.append(el)  # Appends valid data to new list

for el in data_processed:  # Appends values of the queues for particular year to the list
    if el["year"] == year_input:
        queues.append(el["doctor_queue"])
        queues.append(el["nurse_queue"])

result = sum(queues) / len(queues)  # Counts average value of list with queues
print(round(result, 2))
