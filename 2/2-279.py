def f( x, y, z, w ):
  return ((x <= y) <= z) or (not w)

from itertools import *

for a1,a2, a3, a4, a5, a6, a7 in product([0,1], repeat=7):
   tbl = [(a1, 0, a2, 0), (1, a3, a4, a5), (0, 1, a6, a7)]
   if len(tbl) == len(set(tbl)):
      for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in tbl] == [0, 0, 0]:
          print( ''.join(p) )