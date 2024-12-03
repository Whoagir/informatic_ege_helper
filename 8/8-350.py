from itertools import product

A = 'ГАЛАКТИКА'
gl = 'АИ'
count = 0
for w in set(product(A, repeat=8)):
  w = ''.join(w)
  if w[0] not in gl and w[-1] in gl and 'КЛ' not in w:
    count += 1
print( count )