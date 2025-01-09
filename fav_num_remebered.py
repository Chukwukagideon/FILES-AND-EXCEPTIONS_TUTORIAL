""" Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works."""


import json


def get_stored_fav_number():
    """get the stored favorite number if available"""
    try:
        filename = "fav_number.json"
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_number


def get_new_fav_number():
    """prompt user for new favorite number"""
    favorite_number = int(input("What is your favorite number? "))
    filename = "fav_number.json"
    with open(filename, "w") as f:
        json.dump(favorite_number, f)

    return favorite_number


def show_fav_number():
    fav_number = get_stored_fav_number()

    if fav_number:
        print(f"I know your favorite number! It’s {fav_number}")
    else:
        fav_number = get_new_fav_number()
        print(f"I will remember your favorite number next time!")


show_fav_number()

