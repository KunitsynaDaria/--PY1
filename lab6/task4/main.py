import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimited=",", new_line="\n") -> list[dict]:
    new_list = []
    list_dict = []
    with open(filename) as inp:
        for lines in inp:
            line = lines.split(delimited)
            line[len(line) - 1] = line[len(line) - 1][:-1]
            new_list.append(line)
        for i in range(1, len(new_list)):
            dict_ = {}
            for j in range(len(line)):
                dict_[new_list[0][j]] = new_list[i][j]
            list_dict.append(dict_)
    return list_dict

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
