# Reading an entire file
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
print(contents)
# print(contents.rstrip())
print()


# Reading line by line
filename = "pi_digits.txt"

with open(filename) as file_object2:
    for line in file_object2:
        # print(line)
        print(line.rstrip())
print()


# Making a list from a file
with open(filename) as file_object3:
    lines = file_object3.readlines()
print(lines)

for line in lines:
    print(line.rstrip())
print()

# Working with a file's content
with open(filename) as file_object4:
    lines = file_object4.readlines()

pi_string = ""
PI_STRING = ""

for line in lines:
    pi_string += line.rstrip()

#     Remove spaces in between by using the strip() method
    PI_STRING += line.strip()


print(pi_string)
print(len(pi_string))
print(PI_STRING)
print(len(PI_STRING))
