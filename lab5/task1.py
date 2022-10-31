from pprint import pprint


list_numbers = [[bin(i) for i in range(16)], [i for i in range(16)], [hex(i) for i in range(16)], [oct(i) for i in range(16)]]
list_systems = ["bin", "dec", "hex", "oct"]
list_dicts = [{list_systems[i]: list_numbers[i][j] for i in range(4)} for j in range(16)]
pprint(list_dicts)
