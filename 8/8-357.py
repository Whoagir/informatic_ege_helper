from itertools import permutations

A = sorted('КОНДРАТ')
for i, w in enumerate(permutations(A)):
  if i < 3:
    print( f"{i+1}. {''.join(w)}" )
  if i + 1 == 2233:
    print( ''.join(w) )