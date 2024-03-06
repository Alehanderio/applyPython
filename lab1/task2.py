import sys

def no_double_no_space(input_string):
    without_spaces = input_string.replace(" ", "")

    unique_characters = ''.join(sorted(set(without_spaces), key=without_spaces.index))
    print (unique_characters)


input_string = ""

while input_string.lower() != "exit":
    input_string = input("Enter a string: ")

    if input_string.lower() == "exit":
        sys.exit()

    no_double_no_space(input_string)