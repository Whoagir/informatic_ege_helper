from itertools import product

def f( x, y, z, w ):
  return ((not x) <= y) and ((not y) == z) and w

print('x y z w F')
for x, y, z, w in product( [0,1], repeat=4 ):
   if f( x, y, z, w ) == 1:
     print( *map(int, [x, y, z, w, 1]) )

print('\nz x y w F')
for z, y, x, w in product( [0,1], repeat=4 ):
   if f( x, y, z, w ) == 1:
     print( *map(int, [z, y, x, w, 1]) )
