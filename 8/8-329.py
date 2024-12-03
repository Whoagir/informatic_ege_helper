from itertools import product

A = 'ТИМОФЕЙ'
Glas = 'ИОЕ'
Sogl = 'ТМФЙ'

count = 0
for w in set(product(A, repeat = 6)):
  nGlas = sum( 1 for c in w if c in Glas )
  nSogl = sum( 1 for c in w if c in Sogl )
  if nGlas == nSogl:
    count += 1

print( count )



