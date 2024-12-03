from itertools import product

A = sorted('СТЕКЛО')

for i, w in enumerate(product(A, repeat = 5)):
   if w[0] == 'С' and 'ОО' in ''.join(w):
      print( i+1 )
      break

