def create_dictionary(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length")

    result_dictionary = {key: value for key, value in zip(list1, list2)}

    return result_dictionary


lenTemp = int(input("Enter an integer: "))
int_array = [lenTemp]
sec_array = [lenTemp]
print("Fill first array: ")
for i in range(lenTemp):
    int_array.append(int(input("Enter next int: ")))

print("Fill second array: ")
for i in range(lenTemp):
    int_array.append(int(input("Enter next int: ")))


res = create_dictionary(int_array, sec_array)
print(res)