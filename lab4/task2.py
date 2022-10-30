def get_count_char(str_):
    letters_list = list(str_.lower())
    letters_dict = {}

    for letter in letters_list:
        if letter in letters_dict:
            letters_dict[letter] += 1  # оценку уже встречали, поэтому увеличиваем количество
        elif letter.isalpha():
            letters_dict[letter] = 1  # оценку встретили 1 раз

    return letters_dict


def get_percent_char(dict_):
    length = sum(dict_.values())
    for letter in dict_:
        dict_[letter] = round(dict_.get(letter) * 100 / length, 1)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
