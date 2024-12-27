"""A simple addition calculator that handles d ValueError exception
that occurs when a user inputs a string"""

print("Give me ant 2 numbers and i will add them\n")

while True:
    first_number = input("first number: ").lower()
    # condition to be met for breaking the loop
    if first_number == "off":
        break

    second_number = input("second number: ").lower()
    if second_number == "off":
        break

    # add a try except block to catch any ValueError that may occur
    # when user tries to add alphabets with numbers
    try:
        add = int(first_number) + int(second_number)
    except ValueError:
        print("you can only add numbers.")
    else:
        print(f"This is the sum: {add}\n")