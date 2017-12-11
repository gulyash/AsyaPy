# this time instead of one value in the dict we store three values (as a list)
from math import sqrt

word_dict = {}
for i in range(3):
    sentence = input().split()
    for w in sentence:
        if w not in word_dict.keys():
            word_dict[w] = [0, 0, 0]
        word_dict[w][i] += 1

print(word_dict)

# d12 - euclidian distance between first and second vectors and so on
# see the formula in the wikipedia: https://en.wikipedia.org/wiki/Euclidean_distance
d12 = sqrt(sum(pow(word_dict[w][0] - word_dict[w][1], 2) for w in word_dict.keys()))
print(d12)
d23 = sqrt(sum(pow(word_dict[w][1] - word_dict[w][2], 2) for w in word_dict.keys()))
print(d23)
d13 = sqrt(sum(pow(word_dict[w][0] - word_dict[w][2], 2) for w in word_dict.keys()))
print(d12)
