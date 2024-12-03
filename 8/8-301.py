from itertools import product

count = 0
for n in set(product( 'КОМПЬЮТЕР', repeat=5 )):
  setN = set(n)
  freq = [ n.count(c) for c in setN ]
  if sum( 1 for f in freq if f % 2 == 1) == 1:
     count += 1

print( count )