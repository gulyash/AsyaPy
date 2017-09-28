def discriminant():
    return pow(b, 2) - 4 * a * c


def roots():
    x1 = (- b + pow(discriminant(), 0.5)) / (2 * a)
    x2 = (- b - pow(discriminant(), 0.5)) / (2 * a)
    if x1 != x2 :
        return [str(x1), str(x2)]
    else:
        return [str(x1)]


def solve():
    if discriminant() < 0:
        return 'This equation has no roots!'
    else:
        return 'Roots: ' + ' '.join(roots())


print("A: ")
a = float(input())
print("B: ")
b = float(input())
print("C: ")
c = float(input())
print(solve())

