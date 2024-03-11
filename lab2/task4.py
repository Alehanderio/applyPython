def even_numbers_iterator(start, end):
    return (x for x in range(start, end + 1) if x % 2 == 0)

try:
    start = int(input("Input start of range: "))
    end = int(input("Input end of range: "))

    if start <= end:
        even_numbers_iter = even_numbers_iterator(start, end)

        print("All even nums:")
        for num in even_numbers_iter:
            print(num)
    else:
        print("Wrong values for start and end")
except ValueError:
    print("Wrong type of input")
