def counter_of_text(text: str):
    dict = {}
    text_array = text.split()
    for word in text_array:
        dict[word] = dict.get(word, 0) + 1

    print("Статистика унікальних слів:")
    for word, count in dict.items():
        print(f"{word}: {count}")

user_text = input("Введіть текст: ")

counter_of_text(user_text)