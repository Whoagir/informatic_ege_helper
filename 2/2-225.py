def f( x, y, z, w):
  return (y or x) == ((y <= w) or not z)

from itertools import product

for x, y, z, w in product([False, True], repeat=4):
    if not f(x, y, z, w):
       print( int(x), int(y), int(z), int(w) )