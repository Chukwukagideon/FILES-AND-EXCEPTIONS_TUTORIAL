"""Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file."""

from datetime import datetime



filename = "guest_book.txt"
with open(filename, "a") as file_object:
    file_object.write("GUEST NAME | TIME OF ENTRY\n")


while True:
    guest_name = input("Please insert your name: ").title()


    if guest_name == "end".title():
        break


    with open(filename, "a") as file_object:
        current_time = datetime.now().time()
        formatted_time = current_time.strftime("%H:%M:%S")
        file_object.write(f"{guest_name} | {formatted_time}\n")

    print(f"You are welcome, {guest_name}")

