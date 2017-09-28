print('Input 3 values:')
a = int(input())
b = int(input())
c = int(input())

if a <= b <= c:
    a = pow(a, 2)
    b = pow(b, 2)
    c = pow(c, 2)
elif a > b > c:
    b = a
    c = a
else:
    print("Error")
print(a, ' ', b, ' ', c)
