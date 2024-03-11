def generate_min_max_numbers(input_number):
    if 1000 <= input_number <= 9999:
        digits = [int(digit) for digit in str(input_number)]

        sorted_digits = sorted(digits, key=lambda x: (x != 0, x))
        no_zeros = [digit for digit in sorted_digits if digit != 0]

        if (len(no_zeros) < 4):
            no_zeros[1:1]=[0]*(4-len(no_zeros))
        min_number = int(''.join(map(str, no_zeros)))

        max_number = int(''.join(map(str, sorted(digits, reverse=True))))

        return min_number, max_number
    else:
        raise ValueError("Please enter a four-digit positive number.")



try:
    input_number = int(input("Enter a four-digit positive number: "))
    min_result, max_result = generate_min_max_numbers(input_number)
    print(f"Minimum number: {min_result}")
    print(f"Maximum number: {max_result}")
except ValueError:
    print("Invalid input. Please enter a four-digit positive number.")
