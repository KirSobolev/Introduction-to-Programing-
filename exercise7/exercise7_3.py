shopcart = [
    {"name": "Beehive - lamp", "price": 999.9},
    {"name": "Malm - bed", "price": 169.9},
    {"name": "Moomin - mug set", "price": 59.9},
    {"name": "Nemo - divan", "price": 699.9},
    {"name": "Ritz - armchair", "price": 369.9},
]
total_sum = sum([el["price"] for el in shopcart])  # Generates list of price integers and calculates the sum
names_list = [el['name'] for el in shopcart]  # Generates a list with only names
vat = total_sum - total_sum / 1.24  # Calculates 24% VAT

print("Receipt:")
for el in names_list:
    print(f"- {el}")
print(f"\nTotal sum: {total_sum} €.\n"
      f"VAT: {round(vat, 2)} €.\n"
      f"Please come again!")
