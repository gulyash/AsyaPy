line = input('Input Latin string: ')
ellipsis_count = line.count('...')
dots_count = line.count('.') - ellipsis_count * 3
count = sum(line.count(c) for c in ['!', '?'])
print('Number of sentences: ' + str(ellipsis_count + dots_count + count))
