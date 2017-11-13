word_list = ((input('Please input Latin string: ')).lower()).split()
print(min((word for word in word_list if word), key=len))
