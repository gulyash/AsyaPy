import math


while True:
    print('Calculate 4.2 % 2. What is the answer?')
    answer = float(input())
    correctAnswer = 4.2 % 2
    if math.isclose(answer, float(correctAnswer), abs_tol=0.0001):  # https://docs.python.org/3/library/math.html
        print('Your answer is correct.')
        break
    else:
        if answer < correctAnswer:
            print("Your answer is too small.")
        else:
            print("Your answer is too bog.")