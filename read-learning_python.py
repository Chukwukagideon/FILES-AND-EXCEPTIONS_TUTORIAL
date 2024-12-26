# print the contents of the file by reading the entire file
filename = "learning_python.txt"
with open(filename) as file_object:
    contents = file_object.read()

print(contents)
print()


# print contents of the file by looping over the file object
with open(filename) as file_object2:
    for line in file_object2:
        print(line.strip())

print()


# print contents of the file by storing the lines in a list and then working with them outside
# the with block
with open(filename) as file_object3:
    # create a list to store each lines from the file
    lines = file_object3.readlines()
    print(lines)

# storing the lines in a single string.
single_line = ""
for line in lines:
    single_line += line.strip()
print(single_line)
print()

# looping through each line stored in the list and printing out the content of each line.
for line in lines:
    print(line.strip())


# read the file and Replace the word python with C
with open(filename) as file_object4:
    file_contents = file_object4.read()
    updated_file_contents = file_contents.replace("python", "C")
    print(updated_file_contents.upper())
