from itertools import product

A = sorted('МАНГУСТ')

lastPos = -1
for i, x in enumerate(product(A, repeat=6), 1):
   if x[0] != 'У' and x.count('М') == 2 and x.count('Г') <= 1:
      lastPos = i

print( lastPos )
