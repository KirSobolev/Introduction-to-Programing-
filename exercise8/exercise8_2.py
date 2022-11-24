import colorama
from random import randint

colorama.init(autoreset=True)
number = randint(1, 20)
check = True

while check:
    try:
        user_number = int(input("Guess the number (1-20):"))
        if user_number not in range(1, 21):
            # If given number is not in range 1-20 raises exception and handles it afterwards
            raise ValueError
    except ValueError:
        print("Wrong number!")
        continue

    # Next part checks if given number is the right one.
    if user_number < number:
        print(colorama.Back.BLUE + "Too low.")
    elif user_number > number:
        print(colorama.Back.RED + "Too high.")
    else:
        print(colorama.Back.GREEN + "CONGRATULATIONS!")
        check = False  # Stops the program
