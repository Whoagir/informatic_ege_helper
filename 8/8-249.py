from itertools import product

A = sorted('ПАРУС')

for i, w in enumerate(product(A, repeat = 5)):
   if w[0] == 'У' and 'АА' not in ''.join(w):
      print( i+1 )
      break