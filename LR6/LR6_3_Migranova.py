d = {}
for _ in range(int(input())):
    word, hyphen, translation = input().partition(' - ')
    d[word] = list(translation.split(', '))

reverse_dict = {}
for foreign_word, translations in d.items():
    for word in translations:
        if word not in reverse_dict.keys():
            reverse_dict[word] = []
        reverse_dict[word].append(foreign_word)
for k in reverse_dict.keys():
    print(k + ' - ' + ', '.join(reverse_dict[k]))


