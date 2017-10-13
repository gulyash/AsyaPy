def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_sub(start_number, end_number):
    for cur in fib():
        if cur > end_number: return
        if cur >= start_number:
            yield cur


max_num = int(input("Please input max number: "))
for i in fib_sub(0, max_num):
    print(i)
