"""Write a separate program that reads in this value and prints the message,
“I know your favorite number! It’s _____.”"""


import json

filename = "fav_number.json"
with open(filename) as f:
    fav_number = json.load(f)

print(f"I know your favorite number! It’s {fav_number}")