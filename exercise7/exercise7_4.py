list_dicts = [{"name": "Casablanca", "year": 1942}, {"name": "Forrest Gump", "year": 1994},
              {"name": "Avatar", "year": 2009}, {"name": "Green mile", "year": 1999},
              {"name": "Kingdom of heaven", "year": 2005}, {"name": "Constantine", "year": 2005}]
old_movies = []
new_movies = []

for element in list_dicts:  # Divides movies into two separate lists based on production year
    if element["year"] < 2000:
        old_movies.append(element["name"])
    else:
        new_movies.append(element["name"])

print(f"These movies have been released in year 2000 or later: {', '.join(new_movies)}")
print(f"These movies have been released before the year 2000: {', '.join(old_movies)}")
