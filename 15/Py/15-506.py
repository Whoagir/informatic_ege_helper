def f( x, y, A):
  return (x + y <= 22) or  (y <= x - 6) or (y >= A)

from itertools import product
for A in range(1,10000):
  if all( f(x, y, A) for x, y in product( range(1,100), repeat=2 ) ):
    print(A)
