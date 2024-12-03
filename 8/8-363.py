from itertools import permutations

A = 'ХОЧУНАБЮДЖЕТ'
M = 'SGSGSGSGSSGS'

count = 0
for w in set(permutations(M)):
   w = ''.join(w)
   if 'GGGGG' not in w:
     count += (5*4*3*2*1)*(7*6*5*4*3*2*1)

print( count )
