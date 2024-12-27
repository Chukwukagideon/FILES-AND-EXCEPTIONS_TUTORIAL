# filename = "cats.txt"

def file_reader(filename):
    try:
        with open(filename) as file_object:
            pet_names = file_object.read()
    except FileNotFoundError:
        print(f"Requested {filename} not found!")
    else:
        print(pet_names + "\n")


file_reader("cats.txt")
file_reader("dogs.txt")
