word_to_find = input("Type word to find: ")


def book_reader(filename):
    """A simple function to read the contents of a file & count the appearance of the requested word."""
    with open(filename, encoding="utf-8") as file_object:
        content = file_object.read()
        return content


def word_occurrence(content, word_to_find):
    """A function to show all occurrence of the specified word without the context where it was used."""
    # count the number of times the specified word appeared
    print(f"The word {word_to_find} appears {content.lower().count(word_to_find)} times.")

    # convert the content in the file into a list
    words = content.split()
    # show all occurrence of the requested word
    for word in words:
        if word == word_to_find:
            print(word)


def word_finder(content, word_to_find):
    """A function to find specified words from a file and show the context in which it appears."""

    # splits the text into sentences based on the period and space delimiter and coverts it to a list.
    sentences = content.split(". ")
    occurrence = 0

    for sentence in sentences:
        if word_to_find.lower() in sentence.lower():
            occurrence += 1
            print(f"Appearances {occurrence} : {sentence}")
    print(f"\nTotal number of appearance: {occurrence}")


print()

read_book = book_reader("spirit of iron.txt")
word_occurrence(read_book, word_to_find)
print()

word_finder(read_book, word_to_find)