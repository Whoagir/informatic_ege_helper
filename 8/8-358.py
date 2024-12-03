from itertools import permutations

A = sorted('ДОБРЫНЯ')
for i, w in enumerate(permutations(A)):
  if i < 3:
    print( f"{i+1}. {''.join(w)}" )
  if i + 1 == 3377:
    print( ''.join(w) )