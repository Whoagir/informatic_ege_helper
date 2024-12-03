len3 = len( [0, 3, 6, 9] )
lenX3 = 12 - len3

count = 0
for n in range(1,12):
  count += lenX3*len3*lenX3*len3*lenX3*len3

print( count )

# Вариант 2

from itertools import product

count = 0
for n in product( range(12), repeat=7 ):
  if n[0] != 0 and all(
         (a % 3 == 0) ^ (b % 3 == 0)
         for a, b in zip(n, n[1:])):
    count += 1

print( count )