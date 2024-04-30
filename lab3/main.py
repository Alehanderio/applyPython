import sequence_generation
import sequence_operations
import file_operations

def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    sequence = sequence_generation.generate_sequence(rows, columns)
    print("Generated Sequence:")
    sequence_operations.print_sequence(sequence)

    average = sequence_operations.calculate_average(sequence)
    zero_count = sequence_operations.count_zeros(sequence)

    print("\nAverage: {}".format(average))
    print("Zero count: {}".format(zero_count))

    binary_filename = "sequence_data.bin"
    text_filename = "sequence_data.txt"

    file_operations.write_to_binary_file(sequence, average, zero_count, binary_filename)
    file_operations.write_to_text_file(sequence, average, zero_count, text_filename)

    print("\nData written to binary file: {}".format(binary_filename))
    print("Data written to text file: {}".format(text_filename))

if __name__ == "__main__":
    main()
