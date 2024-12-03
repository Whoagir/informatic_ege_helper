from itertools import permutations

A = sorted('МОДЕСТ')
for i, w in enumerate(permutations(A)):
  if i < 3:
    print( f"{i+1}. {''.join(w)}" )
  if i + 1 == 377:
    print( ''.join(w) )