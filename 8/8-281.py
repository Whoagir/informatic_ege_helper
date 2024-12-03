from itertools import product
from string import ascii_uppercase

count = 0
for x in product(ascii_uppercase, repeat=5):
  count += sum( 1 for c in x if c in 'AEOIUY' )

print(count)
