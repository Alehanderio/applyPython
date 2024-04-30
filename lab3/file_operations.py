import pickle

def write_to_binary_file(sequence, average, zero_count, filename):
    with open(filename, 'wb') as file:
        pickle.dump({"sequence": sequence, "average": average, "zero_count": zero_count}, file)

def read_from_binary_file(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data

def write_to_text_file(sequence, average, zero_count, filename):
    with open(filename, 'w') as file:
        file.write("Sequence:\n")
        for row in sequence:
            file.write(str(row) + '\n')
        file.write("\nAverage: {}\n".format(average))
        file.write("Zero count: {}\n".format(zero_count))
