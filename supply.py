from dictioner import lists_dict
from number_generator import nums


def supplier(section):
    x = nums()
    if section in lists_dict:
        for i in x:
            lists_dict[section].append(i)
