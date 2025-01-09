"""Practicing how to use the JSON module"""

"""
# a simple code to ask users for their name and store it in a json file, so it can be read back 
# into memory later on.
import json

username = input("What is your name? ")

filename = "username.json"

with open(filename, "w") as file_object:
    json.dump(username, file_object)
    print("We will remember your name next time!")"""


# using the try except block to attempt to recover a username and if the username is not saved
# it prompts the user to input their name.

import json

filename = "username.json"

try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What is your name? ")
    print("We will remember your name next time")

    with open(filename, "w") as file_object:
        json.dump(username, file_object)
else:
    print(f"Welcome back {username}")