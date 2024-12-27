def book_reader(filename):
    """A simple function to read the contents of a file."""
    with open(filename, encoding="utf-8") as file_object:
       content = file_object.read()
       # count the number of times the specified word appeared
       print(f"The word 'the' appears {content.lower().count("the")} times.")
       print(f"The word 'the ' appears {content.lower().count("the ")} times.")

    words = content.split()
    print(f"The file {filename}, has {len(words)} words.")



book_reader("spirit of iron.txt")
