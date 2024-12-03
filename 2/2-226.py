def f(x, y, z):
  return not (z or x) or(y and not x and ((z and y) <=z))

from itertools import product
for x, y, z in product([False, True], repeat=3):
  if f(x, y, z):
    print( int(x), int(y), int(z) )