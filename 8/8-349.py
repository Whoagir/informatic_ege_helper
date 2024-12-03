from itertools import product

A = 'ДЕВИАЦИЯ'
gl = 'ЕИАЯ'
count = 0
for w in set(product(A, repeat=8)):
  w = ''.join(w)
  if w[0] in gl and w[-1] not in gl and 'ДЕ' in w :
    count += 1
print( count )