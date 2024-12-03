from itertools import product

def f( x, y, z, w ):
  return ((x <= z) <= y) or not w

#print('x y z w F')
print('z x y w F')
for x, y, z, w in product( [0,1], repeat=4 ):
   if f( x, y, z, w ) == 0:
     #print( *map(int, [x, y, z, w, 0]) )
     print( *map(int, [z, x, y, w, 0]) )