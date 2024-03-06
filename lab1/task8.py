translit_dict_eng_to_ukr = {
    'a': 'а', 'A': 'А',
    'b': 'б', 'B': 'Б',
    'c': 'к', 'C': 'К',
    'd': 'д', 'D': 'Д',
    'e': 'е', 'E': 'Е',
    'f': 'ф', 'F': 'Ф',
    'g': 'г', 'G': 'Г',
    'h': 'г', 'H': 'Г',
    'i': 'і', 'I': 'І',
    'j': 'дж', 'J': 'Дж',
    'k': 'к', 'K': 'К',
    'l': 'л', 'L': 'Л',
    'm': 'м', 'M': 'М',
    'n': 'н', 'N': 'Н',
    'o': 'о', 'O': 'О',
    'p': 'п', 'P': 'П',
    'q': 'к', 'Q': 'К',
    'r': 'р', 'R': 'Р',
    's': 'с', 'S': 'С',
    't': 'т', 'T': 'Т',
    'u': 'у', 'U': 'У',
    'v': 'в', 'V': 'В',
    'w': 'уо', 'W': 'Уо',
    'x': 'кс', 'X': 'Кс',
    'y': 'и', 'Y': 'И',
    'z': 'з', 'Z': 'З',
}

translit_dict_ukr_to_eng = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g',
    'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z',
    'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k',
    'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
    'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ь': '', 'ю': 'yu', 'я': 'a',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G',
    'Д': 'D', 'Е': 'E', 'Є': 'Ye', 'Ж': 'Zh', 'З': 'Z',
    'И': 'Y', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P',
    'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F',
    'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
    'Ь': '', 'Ю': 'Yu', 'Я': 'Ya'
    }


def transliterate(dict ,text):

    # Transliterate each character in the text
    translit_text = ''.join(dict.get(char, char) for char in text)

    return translit_text


input_text = input("Enter the text for transliteration: ")

if (input_text[0] in translit_dict_eng_to_ukr):
    transliterated_text = transliterate(translit_dict_eng_to_ukr, input_text)
else:
    transliterated_text = transliterate(translit_dict_ukr_to_eng, input_text)

print("Transliterated text:", transliterated_text)
