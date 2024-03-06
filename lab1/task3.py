import sys

def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0
    total_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
            total_count += 1
        elif char.islower():
            lower_count += 1
            total_count += 1
          
    print (f"Upper: {round(upper_count/total_count, 2)}")
    print (f"Lower: {round(lower_count/total_count, 2)}")


input_string = ""

while input_string.lower() != "exit":
    input_string = input("Enter a string: ")

    if input_string.lower() == "exit":
        sys.exit()

    count_upper_lower(input_string)