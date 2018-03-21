import random

from LR7.Migranova import cut_list, find, bin_to_dec, k_num

string = 'New York is a wonderful city'
slist = ['nice', 'wonderful', 'beautiful', 'gorgeous', 'terrific', 'magnificent', 'amazing', 'grand']
message = '1101100010010'


def cipher(string, slist, message, key):
    # представление строки string в виде списка слов
    str_list = string.split()
    slist = cut_list(slist)
    # пара индексов (synonym_indices):
    # индекс слова word (word_i) в списке слов str_list и индекс его синонима в списке синонимов slist (synonym_i)
    synonym_indices = find(list_a=str_list, list_b=slist)
    for word_i, synonym_i in synonym_indices:
        # алгоритм смотри в задании
        r = random.randrange(0, len(slist))
        k = k_num(slist)
        m = bin_to_dec(message[:k])
        message = message[k:]
        t = (r + m) % len(slist)
        # заменяем слово
        str_list[word_i] = slist[t]
        # склеиваем обратно новую строку из списка слов
        string = ' '.join(str_list)
    return string, message


print(*cipher(string, slist, message, ''), sep='\n')
