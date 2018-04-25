import sys
from collections import Counter


def mega_dict(list_of_dicts):
    dict_0 = list_of_dicts[0]
    dict_1 = list_of_dicts[1]
    dict_2 = list_of_dicts[2]
    # (set(dict_0).union(dict_1)).union(dict_2) - huge dict with all values from all dicts
    # dict_0.get(key, 0) + dict_1.get(key, 0) + dict_2.get(key, 0) - sum of val with this key in all dicts
    # {key: value} - dict initialization
    cool_dict = {key: dict_0.get(key, 0) + dict_1.get(key, 0) + dict_2.get(key, 0) for key in
            (set(dict_0).union(dict_1)).union(dict_2)}


    # cool_dict.items() - key, value
    # 'separator'.join(iterable)
    # k + ' ' + str(v) - 1 line
    return '\n'.join(k + ' ' + str(v) for k, v in cool_dict.items())

def freq1(sents):
    rates = []
    for sentence in sents:
        counts = dict(Counter(sentence))
        rates.append(counts)
    return mega_dict(rates)


def freq2(sentences):
    bigram_list = []
    for sentence in sentences:

        bigram_dict = {}
        for i in range(len(sentence) - 1):
            bigram = ' '.join(sentence[i:i + 2])
            bigram_dict[bigram] = bigram_dict.get(bigram, 0) + 1
        bigram_list.append(bigram_dict)

    return mega_dict(bigram_list)


def freq3(sentences):
    trigram_list = []
    for sentence in sentences:
        trigram_dict = {}
        if len(sentence) > 2:
            for i in range(len(sentence) - 2):
                trigram = ' '.join(sentence[i: i + 3])
                trigram_dict[trigram] = trigram_dict.get(trigram, 0) + 1
        trigram_list.append(trigram_dict)
    return mega_dict(trigram_list)


try:
    input_file_path = sys.argv[1]
    print('Reading fron file: ', input_file_path)
    n = int(sys.argv[2])
    print('N: ', n)

    sentences = []
    try:
        with open(input_file_path) as f:
            for _ in range(3):
                line = f.readline()
                sentences.append(list(word.lower() for word in line.split()))
        print(sentences)

        if n == 1:
            output_file_name = input_file_path + '_1-grams'
            with open(output_file_name, 'w') as output:
                output.write(str(freq1(sentences)))
        elif n == 2:
            output_file_name = input_file_path + '_2-grams'
            with open(output_file_name, 'w') as output:
                output.write(str(freq2(sentences)))
        elif n == 3:
            output_file_name = input_file_path + '_3-grams'
            with open(output_file_name, 'w') as output:
                output.write(str(freq3(sentences)))
        else:
            print('Go fuck yourself.')

    except FileNotFoundError:
        print('File not found.')
except IndexError:
    print('Wrong command line arguments.')
