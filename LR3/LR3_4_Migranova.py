while True:
    print('Calculate 4.2 % 2. What is the answer?')
    answer = float(input())
    correctAnswer = 4.2 % 2
    if abs(answer-float(correctAnswer)) <= 0.0001:
        print('Your answer is correct.')
        break
    else:
        if answer < correctAnswer:
            print("Your answer is too small.")
        else:
            print("Your answer is too big.")
