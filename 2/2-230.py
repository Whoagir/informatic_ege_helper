from itertools import product

def f( x, y, z, w ):
  return (not(x) and y) or (z and not y) or (not z and w)

print('x y z w F')
for x, y, z, w in product( [0,1], repeat=4 ):
   if f( x, y, z, w ) == 0:
     print( *map(int, [x, y, z, w, 0]) )
