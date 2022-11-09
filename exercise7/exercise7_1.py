cafe = {
    "name": "Imaginary Cafe Ltd.",
    "website": "https://edu.frostbit.fi/sites/cafe/en",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"],
    "location": {
        "city": "Rovaniemi",
        "address": "Test address 22",
        "zip_code": "FI-96100"
    }
}
# Joining categories to the string
services = [el for el in cafe['categories']]
services = ", ".join(services)
# BTW question.
# What is better general approach: should I use same variable here for services list and then joining to string
# Or should I use different variables for that f.e. services_list and services_str?

print(f"{cafe['name']}\n"
      f"{cafe['location']['address']}\n"
      f"{cafe['location']['zip_code']} {cafe['location']['city']}\n\n"
      f"{cafe['website']}\n"
      f"Services: {services}")
