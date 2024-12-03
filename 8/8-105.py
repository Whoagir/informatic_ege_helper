from itertools import permutations

A = "НОБЕЛИЙ"

p = [ ''.join(x) for x in permutations(A) ]

count = 0
for x in p:
  if x[0] != 'Й' and 'ИЙО' not in x:
    count += 1

print( count )
