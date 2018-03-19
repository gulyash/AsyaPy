list1 = ['New', 'York', 'is', 'a', 'wonderful', 'and', 'magnificent', 'city']
list2 = ['nice', 'wonderful', 'beautiful', 'gorgeous', 'terrific', 'magnificent', 'amazing', 'grand']


def find(list_a, list_b):
    # a, b - элементы списков list1 и list2 соответсвенно
    # index_a, index_b - индексы элементов списков list_a и list_b соответсвенно
    # enumerate - сопоставляет к каждому элементу списка его индекс, т.е. пронумеровывает слова.
    # Например, для первого списка:
    # (0, 'New'), (1, 'York'), (2, 'is'), (3, 'a'), (4, 'wonderful'), (5, 'and') и т.д.

    # Cмотрим в начало строки: возвращаем пару значений (index_a, index_b) - индексы текущих элементов

    # for (index_a, a) in enumerate(list_a) -
    # для каждой пары значений (индекс_эл-а_1_списка, эл-т_первого_списка)
    # for (index_b, b) in enumerate(list_b) -
    # сопоставляем с каждой парой значений (индекс_эл-а_2_списка, эл-т_второго_списка)

    # Смотри условие в конце строки: если элемент первого списка a равен элементу второго списка b,

    # Т.е. берем один элемент из первого списка, поочередно проверяем его на равенство с каждым элементом второго списка
    # Если элементы равны - возвращаем их индексы парой.

    return [(index_a, index_b) for (index_a, a) in enumerate(list_a) for (index_b, b) in enumerate(list_b) if a == b]


print(find(list_a=list1, list_b=list2))
