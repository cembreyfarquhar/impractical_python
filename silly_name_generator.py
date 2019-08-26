# Chance Embrey-Farquhar / August 26, 2019

# Instructions
# 
# Load a list of first names            DONE
# Load a list of surnames               DONE
# Choose a first name at random         
# Assign the name to a variable
# Choose a surname at random
# Assign the name to a variable
# Print the names to the screen in order and in red font
# Ask the user to quit or play again
# If user plays again:
#  repeat
# If user quits:
#  end and exit                         DONE

import csv
import random 

first_names = []
last_names = []

with open('baby_names.csv', newline='') as csvfile:
    name_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in name_reader:
        name = row[0].split(',')[1].replace('"', '')
        first_names.append(name)

with open('surnames.csv', newline='') as csvfile:
    name_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in name_reader:
        name = row[0].split(',')[0][0] + row[0].split(',')[0].lower()[1:]
        last_names.append(name)

def generate_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = first + " " + last
    return "\033[91m" + name + "\033[0m"

if __name__ == "__main__":
    while True:
        cmd = input("Press enter to generate a name ('q' to quit)")
        if cmd == "q":
            break
        else:
            print(generate_name())