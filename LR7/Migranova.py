from math import floor, log


def find(list_a, list_b):
    return [(index_a, index_b) for (index_a, a) in enumerate(list_a) for (index_b, b) in enumerate(list_b) if a == b]


def bin_to_dec(string):
    return int(string, 2)


def dec_to_bin(i):
    return bin(i)[2:]


def cut_list(list):
    i = floor(log(len(list), 2))
    return list[:2**i]

