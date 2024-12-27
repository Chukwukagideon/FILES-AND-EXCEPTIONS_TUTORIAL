# filename = "cats.txt"

def file_reader(filename):
    """A function to get the file, read and print the contents to the screen"""
    try:
        # open the file as read only
        with open(filename) as file_object:
            pet_names = file_object.read()
    except FileNotFoundError:
        # print(f"Requested {filename} not found!")
        pass # make the code fail silently. i.e. don't give any report to the user, but the code should keep running.
    else:
        print(pet_names + "\n")


file_reader("cats.txt")
file_reader("dogs.txt")
