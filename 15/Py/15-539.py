def F( x, y, A ):
   return (x >= 27) or (2*x < 3*y) or (A > (x+2)*(y-3))

from itertools import product
for A in range(1000):
  if all( F(x,y,A) for x,y in product(range(200), repeat=2) ):
    print(A)
    break
