"""Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____.”"""

import json


favorite_number = int(input("What is your favorite number? "))

filename = "fav_number.json"
with open(filename, "w") as f:
    json.dump(favorite_number, f)
