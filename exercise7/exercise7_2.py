fruits = ("apple", "pear", "banana")
berries = ("strawberry", "blueberry", "blackberry")
vegetables = ("carrot", "kale", "cucumber")
inventory = (fruits, berries, vegetables)

for category in inventory:  # Iterates through categories in inventory
    for element in category:  # Iterates through elements in each category
        print(element)
