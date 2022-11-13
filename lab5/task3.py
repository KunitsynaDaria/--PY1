from random import randint


def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 10
    count = 15
    list_ = []
    while len(list_) < count:
        a = randint(start, stop)
        if a not in list_:
            list_ = list_ + [a]
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
