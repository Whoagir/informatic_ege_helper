from itertools import permutations

A = 'ВОДОПАД'
prohibited = 'ООАО'

count = 0
for w in set(permutations(A)):
  if all( ''.join(pair) not in prohibited
          for pair in zip(w,w[1:])  ) :
    count += 1

print( count )



