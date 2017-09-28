
def are_pretty_much_the_same(a1, a2):
    if abs(float(a1) - float(a2)) < 0.001:  # допустимая погрешность
        return True
    else:
        return False


def check(a1, a2):
    global correctCount
    if are_pretty_much_the_same(a1, a2):  # допустимая погрешность
        print('Your answer is correct.')
        correctCount += 1
    else:
        print('Your answer is incorrect.')


correctCount = 0

print('Calculate 4.2 % 2. What is the answer?')
answer = input()
correctAnswer = 4.2 % 2
print('Your input: ' + answer + '. Correct answer: ' + str(correctAnswer))
check(answer, correctAnswer)

print('Calculate 364 / 4 + 125.4 - 20.8 * 5. What is the answer?')
answer = input()
correctAnswer = 364 / 4 + 125.4 - 20.8 * 5
print('Your input: ' + answer + '. Correct answer: ' + str(correctAnswer))
check(float(answer), correctAnswer)

print('Calculate 25 + 34 * 2 - 9 / 3. What is the answer?')
answer = input()
correctAnswer = 25 + 34 * 2 - 9 / 3
print('Your input: ' + answer + '. Correct answer: ' + str(correctAnswer))
check(float(answer), correctAnswer)

print('Calculate 55.2 - 14 * 2 + 78.3 - 89. What is the answer?')
answer = input()
correctAnswer = 55.2 - 14 * 2 + 78.3 - 89
print('Your input: ' + answer + '. Correct answer: ' + str(correctAnswer))
check(float(answer), correctAnswer)

print('Calculate 2 + 45 * 5 / 4.2 % 2. What is the answer?')
answer = input()
correctAnswer = 2 + 45 * 5 / 4.2 % 2
print('Your input: ' + answer + '. Correct answer: ' + str(correctAnswer))
check(float(answer), correctAnswer)

print(str(correctCount) + ' correct answers out of 5.')

