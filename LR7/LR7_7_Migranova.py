# this time instead of one value in the dict we store three values (as a list)
from math import sqrt


def eucl_dist(words_dictionary, a, b):
    return sqrt(sum(pow(word_dict[w][a] - word_dict[w][b], 2) for w in words_dictionary.keys()))


def matrix():
    matrix = {}
    for i in range(3):
        sentence = input().split()
        for w in sentence:
            if w not in matrix.keys():
                matrix[w] = [0, 0, 0]
            matrix[w][i] += 1
    return matrix


word_dict = matrix()
print(word_dict)

d12 = eucl_dist(word_dict, 0, 1)
print(d12)
d13 = eucl_dist(word_dict, 0, 2)
print(d13)
d23 = eucl_dist(word_dict, 1, 2)
print(d23)
