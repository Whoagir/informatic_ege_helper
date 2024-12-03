from itertools import product

A = sorted('ЛИСЁНОК')

lastPos = -1
for i, x in enumerate(product(A, repeat=5), 1):
   if x[0] != 'О' and x.count('Ё') >= 2 and x[1] == 'К':
      lastPos = i

print( lastPos )
