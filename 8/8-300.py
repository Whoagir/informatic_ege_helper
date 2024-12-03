from itertools import product

count = 0
for n in set(product( 'ДЕРЕВО', repeat=6 )):
  n0 = list(n[0::2])
  n1 = list(n[1::2])
  if n0 == sorted(n0) and n1 == sorted(n1):
     count += 1

print( count )