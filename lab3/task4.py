import json

def word_length_statistics(sentence):
    word_lengths = {}
    words = sentence.split()

    for word in words:
        length = len(word)
        if length in word_lengths:
            word_lengths[length] += 1
        else:
            word_lengths[length] = 1

    sorted_word_lengths = dict(sorted(word_lengths.items()))

    return sorted_word_lengths

def main():
    sentence = input("Input a line: ")

    word_length_stats = word_length_statistics(sentence)

    with open("word_length_stats.json", "w") as file:
        json.dump(word_length_stats, file, indent=4)

    print("Writen successfuly to the fiile word_length_stats.json")

if __name__ == "__main__":
    main()
