from functions import show_numbered_list
people = "John Doe, Tina Tester, Ellie Example"
people = people.split(",")  # Separating into list
people = [el.strip() for el in people]  # Removing extra spaces

show_numbered_list("Original order", people)

show_numbered_list("Alphabetical order by first name", sorted(people))

# Converting Firstname Surname to Surname Firstname by splitting each element of the list, reversing it and joining back
people = [" ".join(reversed(el.split(" "))) for el in people]
show_numbered_list("Alphabetical order by last name", sorted(people))
