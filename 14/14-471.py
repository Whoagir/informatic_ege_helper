def val( x, b ):
  n = 0
  for xi in x:
    n = n*b + xi
  return n

def deval( x, p ):
  d = []
  while x:
    d = [x%p] + d
    x //= p
  return d

from itertools import product

results = []
for p in range(9,20):
 print( p )
 for x, y, z, w in product(range(p), repeat=4):
   if x*z == 0: continue
   n1 = val( [z,x,y,x,8], p )
   n2 = val( [x,y,7,2,9], p )
   n = n1 + n2
   d = deval( n, p )
   if d == [w, z, x, 4, 2]:
     results.append( (x, y, z, w, p) )
     print( x, y, z, w, p, val( [x, y, z, w], p) )

print( results )
print( val( results[0][:-1], results[0][-1] ) )