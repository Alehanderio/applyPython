import sys

def calculate_digit_and_letter_count(input_string):
    digit_count = 0
    letter_count = 0

    for char in input_string:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1

    print(f"Number of digits: {digit_count}")
    print(f"Number of letters: {letter_count}")

input_string = ""

while input_string.lower() != "exit":
    input_string = input("Enter a string: ")



    if input_string.lower() == "exit":
        sys.exit()

    calculate_digit_and_letter_count(input_string)
