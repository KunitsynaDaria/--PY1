from random import sample


def get_random_password(n=8) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    alphabet_list = [letter for letter in alphabet]
    password = sample(alphabet_list, n)
    return "".join(password)


print(get_random_password())
