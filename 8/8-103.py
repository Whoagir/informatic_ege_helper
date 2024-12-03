from itertools import permutations

A = "КУПЧИХА"

p = [ ''.join(x) for x in permutations(A) ]

count = 0
for x in p:
  if x[0] != 'Ч' and 'ИАУ' not in x:
    count += 1

print( count )
