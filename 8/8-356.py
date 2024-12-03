from itertools import permutations

A = sorted('ГЕРАСИМ')
for i, w in enumerate(permutations(A)):
  if i < 3:
    print( f"{i+1}. {''.join(w)}" )
  if i + 1 == 1899:
    print( ''.join(w) )