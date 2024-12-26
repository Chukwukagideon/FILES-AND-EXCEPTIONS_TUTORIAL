"""A simple addition calculator that handles d ValueError exception
that occurs when a user inputs a string"""

print("Give me ant 2 numbers and i will add them\n")

try:
    first_number = int(input("first number: "))
    second_number = int(input("second number: "))
except ValueError:
    print("you can only input a number")
else:
    add = first_number + second_number
    print(add)