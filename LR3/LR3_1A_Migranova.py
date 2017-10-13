print("Fibonacci numbers: ")
fib1 = 0
fib2 = 1
n = 20
i = 2
while i < n:
    new_fib = fib1 + fib2
    if i > 4:
        print(new_fib)
    fib1 = fib2
    fib2 = new_fib
    i = i + 1


# было:
# print("Fibonacci numbers: ")
# fib1 = 0
# fib2 = 1
# print(fib1)
# print(fib2)
# n = 10
# i = 2
# while i < n:
#     new_fib = fib1 + fib2
#     print(new_fib)
#     fib1 = fib2
#     fib2 = new_fib
#     i = i + 1
