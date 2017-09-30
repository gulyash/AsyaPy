def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::2]  # от -1 : до конца : с шагом 2
    even_digits = digits[-2::2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10


def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


cardNumOk = False

while not cardNumOk:
    print('Please, input your card number:')
    cardNum = input()
    cardNum = ''.join(cardNum.split())  # this removes spaces if there are any
    if is_luhn_valid(cardNum):
        print('Your card number is: ', ' '.join(cardNum[i:i + 4] for i in range(0, 16, 4)))
        cardNumOk = True
    else:
        print('Not a valid card number (it was checked using Luhn algorithm). \nTry again.')

cvvOk = False

while not cvvOk:
    print('Please, input your CVV:')
    cvv = ''.join(input().split())
    if len(cvv) == 3:
        try:
            cvvInt = int(cvv)
            print('Your CVV is: ' + cvv)
            cvvOk = True
        except ValueError:
            print('Not a number, try again')
    else:
        print('Not 3 characters long, try again')

print('Please, input your name:')
name = input()
print('Your name is: ' + name + '. What a beautiful name!')


expiryOk = False

while not expiryOk:
    print('Please, input your card expiry date:')
    expiry = ''.join(input().split())
    if len(expiry) == 4:
        try:
            expiryInt = int(expiry)
            # http://pythoncentral.io/cutting-and-slicing-strings-in-python/
            nums = [expiry[i:i + 2] for i in range(0, 4, 2)]
            print(nums[:])
            if int(nums[0]) < 32 and int(nums[1]) < 13:
                print('Your card expiry date is:', '.'.join(nums))
                expiryOk = True
            else: print("Not a valid date.")
        except ValueError:
            print('Not a number, try again')
    else:
        print('Not 4 characters long, try again')
