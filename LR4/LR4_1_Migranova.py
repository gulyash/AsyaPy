string = input('Please input Latin string: ')
uppercase = 0
lowercase = 0
for letter in string:
    if letter.islower():
        lowercase += 1
    elif letter.isupper():
        uppercase += 1
uppercase_percentage = uppercase/len(string)*100
lowercase_percentage = lowercase/len(string)*100
print('Uppercase letters: %f%%' % uppercase_percentage)
print('Lowercase letters: %f%%' % lowercase_percentage)
