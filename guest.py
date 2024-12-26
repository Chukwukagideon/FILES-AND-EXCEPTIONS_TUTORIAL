""" Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt."""

guest_name = input("Please type your name here: ").title()

filename = "guest.txt"

with open(filename, "w") as file_object:
    content = f"The name of this guest is {guest_name}.\n"
    file_object.write(content)