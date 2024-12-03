from itertools import product

def f( a, b, c, d ):
  return (a <= b) and (c <= d) or not c

#print('a b c d F')
print('b d c a F')
for a, b, c, d in product( [0,1], repeat=4 ):
   if f( a, b, c, d ) == 0:
     print( *map(int, [b, d, c, a, 0]) )