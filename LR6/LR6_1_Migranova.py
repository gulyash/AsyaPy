sentence = input().split()
word_dict = {}
for w in sentence:
    word_dict[w] = word_dict.get(w, 0) + 1
print('WORDS:')
for k, v in word_dict.items():
    print(k + ' ' + str(v))

bigram_dict = {}
for i in range(len(sentence)-1):
    bigram = ' '.join(sentence[i:i+2])
    bigram_dict[bigram] = bigram_dict.get(bigram, 0) + 1
print('BIGRAMS:')
for k, v in bigram_dict.items():
    print(k + ' ' + str(v))
