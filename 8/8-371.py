from itertools import product

A = sorted(set('УДАЧА'))

k = 0
for w in product(A, repeat=5):
  w = ''.join(w)
  if w[0] in 'АУ':
    k += 1
    if w == 'УДАЧА':
      print( k )
      break
