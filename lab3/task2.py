def count_occurrences(file_path, x):
    occurrences = {}

    with open(file_path, 'r') as file:
        content = file.read()
        
        if isinstance(x, str):
            occurrences[x] = content.count(x)
        elif isinstance(x, list):
            for item in x:
                occurrences[item] = content.count(item)

    return occurrences

file_path = input("Введіть шлях до файлу: ")
x = input("Введіть параметр x (рядок або список через кому): ")

if ',' in x:
    x = x.split(',')
else:
    x = [x]

result = count_occurrences(file_path, x)
print("Частота повторень параметра x у файлі:", result)
