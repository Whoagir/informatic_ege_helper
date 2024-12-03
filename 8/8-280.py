from itertools import product
from string import ascii_uppercase

count=0
for x in product(ascii_uppercase, repeat=5):
  k = sum( 1 for c in x if c in 'AEOIUY' )
  if k > 0:
    count += 1

print(count)


