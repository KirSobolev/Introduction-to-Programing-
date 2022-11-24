import colorama
from datetime import date

# Initialize colorama
colorama.init(autoreset=True)

years = []
today = int(date.today().year)  # Gets current year and makes in integer

for el in range(5):  # Appends years of birth to the list
    try:
        person_index = el + 1  # Keeps track of number of persons
        el = int(input(f"Give the birth year of person {person_index}:"))
    except ValueError:
        print(colorama.Back.RED + "Wrong answer, must be integer")
        continue
    years.append(el)

for el in years:
    result = today - el
    if 0 < result < 125:
        print(f"{colorama.Fore.GREEN}{result} years old, age OK!")
    else:
        print(f"{colorama.Fore.RED}{result} years old, incorrect age")
