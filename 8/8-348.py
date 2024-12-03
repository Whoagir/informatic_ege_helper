from itertools import product

A = sorted(set('ГРАНАТ'))
for i, w in enumerate(product(A, repeat=6), start=1):
  w = ''.join(w)
  if w == 'ГРАНАТ':
    print(i)
    break