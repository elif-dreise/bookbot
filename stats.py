def count_words(text):
    num_words = len(text.split())
    print(f"{num_words} words found in the document")
    return num_words


def num_character(text):
    text_low = text.lower()
    letters = sorted(list(set(list(text_low))))
    # print(letters)
    letter_count = {}
    for letter in letters:
        letter_count.update({letter: 0})
    # print(letter_count)
    for letter in text_low:
        if letter in letter_count:
            letter_count[letter] += 1
    # print(letter_count)
    return letter_count


def sorted_list_dicts(letter_count):
    list_dict = [{char: count} for char, count in letter_count.items()]
    list_dict.sort(key=lambda x: list(x.values())[0], reverse=True)
    # print(list_dict)
    return list_dict




def alpha_sorted_list(list_dict):
 
    for char_dict in list_dict:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")

