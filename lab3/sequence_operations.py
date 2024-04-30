def print_sequence(sequence):
    for row in sequence:
        print(row)

def calculate_average(sequence):
    total = 0
    count = 0
    for row in sequence:
        for num in row:
            total += num
            count += 1
    if count == 0:
        return 0
    return total / count

def count_zeros(sequence):
    zero_count = 0
    for row in sequence:
        zero_count += row.count(0)
    return zero_count
