from itertools import product

for i, w in enumerate(product(sorted('МАРИЯ'), repeat=4), start=1):
  if ''.join(w) == 'АРИЯ':
    print(i)
    break