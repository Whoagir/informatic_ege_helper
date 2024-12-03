from itertools import permutations

A = sorted('ЛЕОНАРД')
for i, w in enumerate(permutations(A)):
  if i < 3:
    print( f"{i+1}. {''.join(w)}" )
  if i + 1 == 4321:
    print( ''.join(w) )