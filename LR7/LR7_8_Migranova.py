# this time instead of one value in the dict we store three values (as a list)
from math import sqrt


def eucl_dist(words_dictionary, a, b):
    return sqrt(sum(pow(word_dict[w][a] - word_dict[w][b], 2) for w in words_dictionary.keys()))


def pearson(wd, x, y):
    average_x = sum(wd[w][x] for w in wd.keys()) / len(wd)
    average_y = sum(wd[w][y] for w in wd.keys()) / len(wd)

    numerator = sum(((wd[i][x] - average_x) * (wd[i][y]- average_y)) for i in wd.keys())
    denominator = sqrt(sum((pow((wd[i][x] - average_x), 2) * (pow((wd[i][y] - average_y), 2)))for i in wd.keys()))

    return numerator/denominator


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
d13 = eucl_dist(word_dict, 0, 2)
d23 = eucl_dist(word_dict, 1, 2)

print('Евклидовы расстояния для предложений: ')
print('1-2: ', d12)
print('1-3: ', d13)
print('2-3: ', d23)



p12 = pearson(word_dict, 0, 1)
p13 = pearson(word_dict, 0, 2)
p23 = pearson(word_dict, 1, 2)

print('Коэффициент корреляции Пирсона для предложений: ')
print('1-2: ', p12)
print('1-3: ', p13)
print('2-3: ', p23)

