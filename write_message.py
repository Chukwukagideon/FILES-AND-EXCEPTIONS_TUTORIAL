# writing to an empty file
# NOTE: the write mode empties the file before returning the file object
filename = "programming.txt"

with open(filename, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Appending to a file
# NOTE: the append mode does not erase the contents of the file before returning the file object.
# It simply adds the new line to the end of the file.
with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.")
    file_object.write("I love writing code and solving problems.")
