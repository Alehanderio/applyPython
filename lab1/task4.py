import sys

def splitty(input_array):
    res_array = []
    for word in input_array:
        res_array.append([char for char in word])
    
    return res_array


input_string = ""

while input_string.lower() != "exit":
    input_string = input("Enter a string: ")
    input_array = input_string.split()

    if input_string.lower() == "exit":
        sys.exit()

    printty = splitty(input_array)
    for elem in printty:
        print(elem)