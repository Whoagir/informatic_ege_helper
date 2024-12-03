def f( x, y, A ):
  return (11 <=y) or (7*y < x) or (A > x*y)

from itertools import product

A = 1
while A < 1000:
  if all( f(x,y,A) for x, y in product(range(200), repeat=2) ):
    print( A )
    break
  A += 1