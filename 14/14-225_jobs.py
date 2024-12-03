# Автор: Е. Джобс

from itertools import product
s = open('24-225.txt').readline()
for x in product(range(9, -1, -1), repeat=5):
    n = '44{}{}78{}{}{}3'.format(*x)
    if n in s:
        print(sum(int(i) for i in n if i in set('02468')))
        break


from itertools import product
s = open('24-225.txt').readline()
words = set(s.split('FF')[1:-1])
for x in product(range(9, -1, -1), repeat=5):
    n = '44{}{}78{}{}{}3'.format(*x)
    if n in words:
        print(4 + 4 + 8 + sum(i for i in x if i % 2 == 0))
        break
