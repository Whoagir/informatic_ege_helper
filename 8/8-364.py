# Автор: Е. Джобс

from itertools import product

A = sorted('АПРЕЛЬ')[::-1]

c = 0
for i, x in enumerate(product(A, repeat=5), 1):
    if x[-1] == 'Ь':
        c += 1
    if i == 387:
        break
print(c)
