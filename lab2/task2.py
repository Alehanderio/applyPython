def read_dicts_from_user():
    list_of_dicts = []
    
    while True:
        user_input = input("Enter a dictionary (in the format key:value, separated by commas), or 'done' to finish: ")

        if user_input.lower() == 'done':
            break

        try:
            new_dict = dict(item.split(':') for item in user_input.split(','))
            list_of_dicts.append(new_dict)
        except ValueError:
            print("Invalid input. Please enter dictionaries in the format key:value, separated by commas.")

    return list_of_dicts

def merge_dicts(list_of_dicts):
    result_dict = {}
    for dictionary in list_of_dicts:
        result_dict.update(dictionary)

    return result_dict

list_of_dicts = []

while True:
    user_input = input("Creating a new dictionary or exit: ")

    if user_input.lower() == 'exit':
        break

    try:
        temp_dict = read_dicts_from_user()
        list_of_dicts.extend(temp_dict)  # Use extend instead of append
    except ValueError:
        print("Invalid input. Please enter dictionaries in the format key:value, separated by commas.")

result = merge_dicts(list_of_dicts)
print(result)
