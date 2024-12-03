from itertools import product

A = sorted('КОМПЬЮТЕР')

lastPos = -1
for i, x in enumerate(product(A, repeat=5), 1):
   if i % 2 == 1 and x[0] != 'Ь' and x.count('К') == 2:
      lastPos = i

print( lastPos )
