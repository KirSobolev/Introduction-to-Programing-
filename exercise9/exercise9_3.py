from functions import magazine_serial_check
import colorama

colorama.init(autoreset=True)

valid = f"{colorama.Fore.GREEN}Valid ISSN"
invalid = f"{colorama.Fore.RED}Incorrect ISSN"
serial = input("Give an ISSN-serial")
if magazine_serial_check(serial):
    print(valid)
else:
    print(invalid)

