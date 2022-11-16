restaurants = [{"name": "North Delish",
                "rating": 4.5,
                "reservations": True,
                "services": ["lunch", "dinner"],
                "price_level": 5,
                "location": "Rovaniemi"},
               {"name": "Food Galore",
                "rating": 3.8,
                "reservations": False,
                "services": ["breakfast", "lunch"],
                "price_level": 3,
                "location": "London"},
               {"name": "Snacksy Ltd",
                "rating": 3.2,
                "reservations": False,
                "services": ["lunch", "dinner", "night"],
                "price_level": 2,
                "location": "Berlin"},
               {"name": "Not Hemingway's",
                "rating": 2,
                "reservations": False,
                "services": ["night"],
                "price_level": 5,
                "location": "Rovaniemi"},
               {"name": "Sale 24",
                "rating": 5,
                "reservations": False,
                "services": ["breakfast", "lunch", "dinner", "night"],
                "price_level": 2,
                "location": "Rovaniemi"}
               ]
check = True
rating_input = None
price_input = None
reservation_input = None
time_input = None
matching_restaurants = []
print("Welcome to restaurant search")
while check:
    # Practising try except here. If statements allow to save already answered questions.
    try:
        if rating_input is None:
            rating_input = int(input("Which star rating at least for the restaurant?(1-5)"))
        if price_input is None:
            price_input = int(input("What is the maximum price level you're looking for? (1-5)"))
        if reservation_input is None:
            reservation_input = input("Would you like to make a reservation before hand? (y/n) ").lower()
        if time_input is None:
            time_input = int(input("In what time would you like to arrive? (0 – 23)"))
            if time_input > 24:
                time_input = None
                raise ValueError
        check = False
    except ValueError:
        print("Invalid answer, try again")
        continue

# Next If statements check for exact service
if time_input in range(6, 11):
    service = "breakfast"
elif time_input in range(11, 17):
    service = "lunch"
elif time_input in range(17, 25):
    service = "dinner"
elif time_input in range(0, 6):
    service = "night"

for restaurant in restaurants:
    if restaurant["rating"] >= rating_input:
        if restaurant["price_level"] <= price_input:
            reservation_check = lambda a: True if a == "y" else False  # Checks if reservation is needed
            if restaurant["reservations"] == reservation_check(reservation_input):
                if service in restaurant["services"]:
                    matching_restaurants.append(restaurant["name"])

if len(matching_restaurants) == 0:
    print("No matching restaurants found, unfortunately!")
else:
    print(f"Matching restaurants are: {', '.join(matching_restaurants)}")
