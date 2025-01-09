"""Practicing how to use the JSON module"""

import json

username = input("What is your name? ")

filename = "username.json"

with open(filename, "w") as file_object:
    json.dump(username, file_object)
    print("We will remember your name next time!")