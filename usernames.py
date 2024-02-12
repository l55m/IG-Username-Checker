from colorama import Fore, init
import random, string
init(autoreset=False)
purple = Fore.MAGENTA
white = Fore.WHITE
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE

output_file = "usernames.txt"
amount = int(input(f"{blue}[^-^]{purple} Strings: "))
character_amount = int(input(f"{blue}[^-^]{purple} Character Amount: "))

for i in range(amount):
    generated = ("").join(random.choices(string.ascii_letters + string.digits, k = character_amount))
    print(generated)
    with open(output_file, "a") as f:
        f.write(generated + "\n")
input()