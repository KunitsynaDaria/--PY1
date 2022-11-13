from random import sample
import string


def get_random_password(n=8) -> str:
    alphabet = string.digits + string.ascii_letters
    alphabet_list = [letter for letter in alphabet]
    password = sample(alphabet_list, n)
    return "".join(password)


print(get_random_password())
