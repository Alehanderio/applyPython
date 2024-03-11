def contains_sequence_123(lst):
    for index in range(len(lst) - 2):
        if [1, 2, 3] == lst[index:index + 3] or \
           [1, 3, 2] == lst[index:index + 3] or \
           [2, 1, 3] == lst[index:index + 3] or \
           [2, 3, 1] == lst[index:index + 3] or \
           [3, 1, 2] == lst[index:index + 3] or \
           [3, 2, 1] == lst[index:index + 3]:
            return True
    return False


# Example usage
#list_1 = [1, 2, 3, 4, 5]
#list_2 = [3, 2, 1, 4, 5]
#list_3 = [5, 4, 3, 2, 1]

#print(contains_sequence_123(list_1))  # True
#print(contains_sequence_123(list_2))  # True
#print(contains_sequence_123(list_3))  # False

lenTemp = int(input("Enter an integer: "))
int_array =[]
for i in range(lenTemp):
    int_array.append(int(input("Enter next int: ")))
print(contains_sequence_123(int_array))