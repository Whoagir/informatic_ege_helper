from itertools import product

A = 'СВЯТОСЛАВ'
Glas = 'ЯОА'
Sogl = 'СВТЛ'

count = 0
for w in set(product(A, repeat = 7)):
  nGlas = sum( 1 for c in w if c in Glas )
  nSogl = sum( 1 for c in w if c in Sogl )
  if nGlas > nSogl:
    count += 1

print( count )



