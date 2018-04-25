from math import floor, log

l = input("Введите список слов через пробел: ").split()


def cut_list(list):
    i = floor(log(len(list), 2))
    return list[:2**i], i


print(cut_list(l))
