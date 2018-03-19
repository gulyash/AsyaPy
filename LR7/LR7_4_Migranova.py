from math import floor, log

l = input("Введите список слов через пробел: ").split()


def cut_list(list):
    length = floor(log(len(l), 2))+1
    return list[:length]


print(cut_list(l))
