print('Input 3 values:')
arr = [int(input()), int(input()), int(input())]

neg = pos = zero = 0
for n in arr:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero +=1
print('\nPositive: ', pos)
print('Negative: ', neg)
print('Zeros: ', zero)

