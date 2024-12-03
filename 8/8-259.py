from itertools import product

def valid( word ):
  ref = 'ВОЛК'
  count = 0
  for i in range(4):
    if word[i] == ref[i]: count += 1
  return count == 2

A = 'ПОЛЯКВ'
count = 0
for word in product(A, repeat=4):
  if valid( word ):
    count += 1

print( count )


