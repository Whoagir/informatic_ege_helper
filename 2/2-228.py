from itertools import product

def f( x, y, z, w ):
  return not (w <= z) or (x <= y) or not x

#print('x y z w F')
print('w z y x F')
for x, y, z, w in product( [0,1], repeat=4 ):
   if f( x, y, z, w ) == 0:
     #print( *map(int, [x, y, z, w, 0]) )
     print( *map(int, [w, z, y, x, 0]) )