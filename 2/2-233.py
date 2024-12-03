def f(x, y, z, w):
    return (z <= x) <= (w or not(y))

from itertools import product

for x, y, z, w in product([0,1], repeat=4):
   if f(x,y,z,w) == 0:
     print( z, x, w, y)
