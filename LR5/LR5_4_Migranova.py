import random # датчик, Карл! датчик!

l1, l2 = [], []
for _ in range(10):
    l1.append(random.randrange(0, 100))
    l2.append(random.randrange(0, 100))
print(*sorted(l1 + l2))

