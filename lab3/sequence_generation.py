import random

def generate_sequence(rows, columns):
    sequence = [[random.randint(-10, 10) for _ in range(columns)] for _ in range(rows)]
    return sequence
