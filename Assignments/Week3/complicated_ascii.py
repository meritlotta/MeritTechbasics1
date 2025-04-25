# More Complicated Ascii
import time
import random

# Drink Colour
YELLOW = "\033[93m"
BLUE = "\033[94m"
BROWN = "\033[33m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Label Colour
RED = "\033[91m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"

# Welcome
print("Today, you will have the chance to create your very own brand of a drink!")
time.sleep(1)

# Enter name of the bottle
print("First you will decide what name it will say on the bottle.")
time.sleep(1)

while True:
    name = input("Please a max. of 12 characters: ")
    if len(name) <= 12:
       break
    print("That is too long. Please enter 12 characters or fewer.")
time.sleep(1)

print("Perfect!")
time.sleep(1)
centered_name = name.center(14)

# Height of the label
print("Now decide how tall your label should be.")
time.sleep(1)

while True:
    height = input("Please enter a number between 1 and 5: ")
    try:
        label_height = int(height)
        if 1 <= label_height <= 5:
            break
        else:
            print("That number is out of range. Please enter a number between 1 and 5.")
    except ValueError:
        print("That's not a valid number. Please enter a number between 1 and 5.")
    time.sleep(1)

top_space = label_height // 2
bottom_space = label_height - top_space

# Create label border
border = "-" * 14

# Liquid in bottle
print("What kind of drink would be inside your bottle?")
time.sleep(1)

valid_drinks = ['mate', 'water', 'juice', 'coffee']

while True:
    liquid = input("Please enter 'mate', 'water', 'juice' or 'coffee': ")
    if liquid in valid_drinks:
        if liquid.lower() == "mate":
            drink_colour = YELLOW
        elif liquid.lower() == "water":
            drink_colour = BLUE
        elif liquid.lower() == "juice":
            drink_colour = CYAN
        elif liquid.lower() == "coffee":
            drink_colour = BROWN
        break
    else:
      print("This is not a valid choice. Please try again.")

liquid_bottom_line = drink_colour + "\\" * 14 + RESET

time.sleep(1)
print("Nice!")

# Label colour
label_colour = [RED, GREEN, MAGENTA]
label_colour = random.choice(label_colour)


# Decorations
deco_colour = [YELLOW, BLUE, BROWN, CYAN, RED, GREEN, MAGENTA]
deco_colour = random.choice(deco_colour)

print("Now its time for decorations!")
time.sleep(1)

# Top Border Decorations
print("Let's start with the top border.")
time.sleep(1)
print("Insert any sign you like!")
time.sleep(1)
while True:
    deco_top = input("Make sure its only a single character: ")
    if len(deco_top) == 1:
         break
    else:
        print("That's too long. Please enter a single character.")

deco_top_line = deco_top * 14

#Bottom Border Decorations
print("Okay perfect, now the bottom border.")
time.sleep(1)
print("Again, insert any sign you like!")

while True:
    deco_bottom = input("And please make sure its only a single character: ")
    if len(deco_bottom) == 1:
           break
    else:
         print("That's too long. Please enter a single character.")



deco_bottom_line =deco_bottom * 14

# Random quote on bottle
quote = ["Est. 2025", "FOR YOU!", "Only now", "Fresh brew", "No sugar", "Made with ❤️", "ENJOY"]
chosen_quote = random.choice(quote)

# Actual printing
# Fix Top of the bottle
print("                ______  ")
print("               |______| ")
print("               |      | ")
print("               |      | ")
print("               |" + drink_colour + "\\" * 6 + RESET + r"| ")
print("               |" + drink_colour + "\\" * 6 + RESET + r"| ")
print("              /" + drink_colour + "\\" * 8 + RESET + r"\ ")
print("             /" + drink_colour + "\\" * 10 + RESET + r"\ ")
print("            /" + drink_colour + "\\" * 12 + RESET + r"\ ")

# Body of the bottle with custom label
print("           |" + chosen_quote.center(14) + "|")

print("           |" + label_colour + border + RESET + "|")
for _ in range(top_space):
    print("           |" + label_colour + "/" * 14 +RESET + "|")
print("           |" + deco_colour + deco_top_line + RESET + "|")

print("           |" + centered_name + "|")
print("           |" + deco_colour + deco_bottom_line + RESET + "|")
for _ in range(bottom_space):
    print("           |" + label_colour + "/" * 14 +RESET + "|")
print("           |" + label_colour + border + RESET + "|")

# Fix bottom part
print("           |" + label_colour + liquid_bottom_line + RESET + "|")
print("           |" + label_colour + liquid_bottom_line + RESET + "|")
print("           |" + label_colour + liquid_bottom_line + RESET + "|")
print(r"            \____________/  ")
