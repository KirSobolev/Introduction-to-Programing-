from colorama import init, Back

init(autoreset=True)  # Initializes colorama
numbers = range(2, 101)

for number in numbers:  # Iterates through all numbers 2-100
    check = False
    for i in range(2, number):  # Iterates through all numbers between 2 and (the number from previous loop - 1)
        if (number % i) == 0:  # Checks if the number is dividable by any other number
            check = True
            break
    if check:
        print(Back.RED + f"{number} is not prime")
    else:
        print(Back.GREEN + f"{number} is prime")
        