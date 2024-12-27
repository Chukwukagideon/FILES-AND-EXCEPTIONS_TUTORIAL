filename = "cats.txt"

with open(filename) as file_object:
    pet_names = file_object.read()

print(pet_names)
