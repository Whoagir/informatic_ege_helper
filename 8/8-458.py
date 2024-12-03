from itertools import product

n = 1
for w in product(sorted('ФОКУС'),repeat=5):
  if w.count('Ф') == 0 and w.count('У') == 2:
     print( n, w )
  n += 1

