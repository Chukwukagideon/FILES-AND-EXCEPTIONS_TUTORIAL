"""Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses."""

while True:
    reason = input("Why do you like programming: ").capitalize()

    if reason == "end".capitalize():
        break
    else:
        filename = "programming_poll_responses.txt"
        with open(filename, "a") as file_object:
            file_object.write(reason + "\n")
