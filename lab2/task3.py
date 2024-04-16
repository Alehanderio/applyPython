check_point = int(input("Enter an int to be compared to: "))
lenTemp = int(input("Enter size of an array: "))
int_array = []
print("Fill the array: ")
for i in range(lenTemp):
    int_array.append(int(input("Enter next int: ")))

res = [num for num in int_array if num > check_point]

print(res)