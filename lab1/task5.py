def squerry(input_array):
    res_array = []
    for num in input_array:
        if (num ** 2) <= 30:
            res_array.append(num)
    
    return res_array

len = int(input("Enter an integer: "))
int_array =[]
for i in range(len):
    int_array.append(int(input("Enter next int: ")))

print(squerry(int_array))