stock = {
    'milk': 2,
    'bread': 4,
    'tomatoes': 1,
    'cheese': 5,
    'sour cream': 2,
    'potato': 9,
    'carrot': 10,
    'apple': 8,
    'cookies': 3,
    'pineapple': 7
}
print(*(k + ': ' + str(stock[k]) for k in stock.keys()), sep='\n')

good = input('Остаток на складе для: ')
print('Равен:', stock[good])

print('Введите три купленных товара и через тире (с пробелами) - их количество:')
for _ in range(3):
    good, delimiter, amount = input().partition(' - ')
    stock[good] -= int(amount)

print('Введите два новых товара и через тире (с пробелами) - их количество:')
for _ in range(2):
    good, delimiter, amount = input().partition(' - ')
    stock[good] = int(amount)

print('Введите наименование распроданного товара:')
stock.pop(input(), None)

print(*(k + ': ' + str(stock[k]) for k in stock.keys()), sep='\n')
