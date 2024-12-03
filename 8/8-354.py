from itertools import permutations

A = sorted('РУСЛАН')
for i, w in enumerate(permutations(A)):
  if i < 3:
    print( f"{i+1}. {''.join(w)}" )
  if i + 1 == 442:
    print( ''.join(w) )