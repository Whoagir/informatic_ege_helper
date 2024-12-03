def f(x, y, z, w):
    return w and ((x <= y) == (y <= z))

from itertools import product

for x, y, z, w in product([0,1], repeat=4):
   if f(x,y,z,w) == 1:
     print( x, z, w, y)
