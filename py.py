
cardNumOk = False

while not cardNumOk:
    print('Please, input your card number:')
    cardNum = input()
    cardNum = ''.join(cardNum.split())  # this removes spaces if there are any
    if len(cardNum) == 16:
        # check if it's a number
        try:
            cardNumInt = int(cardNum)  # this might throw an exception
            print('Your card number is: ', ' '.join(cardNum[i:i + 4] for i in range(0, 16, 4)))
            cardNumOk = True
        except ValueError:
            print('Not a number, try again')
    else:
        print('Not 16 characters long, try again')

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
