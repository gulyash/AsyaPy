def f(x):
    if x <= 0:
        return -x
    elif 0 < x < 2:
        return x*x
    else:
        return 4


arg = float(input('Input real number: ',))
print('Result: ' + str(f(arg)))
