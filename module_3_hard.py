import copy
from importlib.metadata import Lookup


def list_sum(list, total_sum):
    for item in list:
        if isinstance(item, (int, float)):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, set):
            for item in item:
                total_sum += calculate_structure_sum(item)
    return total_sum


def dict_sum(dict, total_sum):
    for key, value in dict.items():
        if isinstance(key, (int, float)):
            total_sum += key
        elif isinstance(key, str):
            total_sum += len(key)
        if isinstance(value, (int, float)):
            total_sum += value
        elif isinstance(value, str):
            total_sum += len(value)
    return total_sum


def calculate_structure_sum(data):
    total_sum = 0

    for i in data:
        if isinstance(i, (list, set)):
            total_sum = list_sum(i, total_sum)
        elif isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, int):
            total_sum += (i)
        elif isinstance(i, (dict)):
            total_sum = dict_sum(i, total_sum)
        elif isinstance(i, tuple):
            total_sum += calculate_structure_sum(list(i))
    return total_sum


data_structure = [
    [1, 2, 3],
    {'s': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
