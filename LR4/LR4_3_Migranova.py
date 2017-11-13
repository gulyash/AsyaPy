word_list = ((input('Please input Latin string: ')).lower()).split()
longest_word = max((word for word in word_list if word), key=len)
print(longest_word.replace('e', 's'))
