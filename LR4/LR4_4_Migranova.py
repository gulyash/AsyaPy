s = input('Введите исходную строку: ')
r = input('Введите подстроку для вставки: ')
left_index = s.find('[')  # самая левая открывающая скобка
right_index = left_index
open_brackets_count = 0
for i, c in enumerate(s[left_index:]):  # enumerate сопоставляет к каждой букве c строки s индекс i
    if c == '[':
        open_brackets_count += 1
    elif c == ']':
        open_brackets_count -= 1
        if open_brackets_count == 0:
            right_index = i + left_index + 1
            break
if right_index > left_index:
    substring = s[left_index:right_index]
    print(s.replace(substring, r))
else:
    print('Wrong brackets.')
