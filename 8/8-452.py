from itertools import product

A = "012345678"

count = 0
for w in sorted(product(A, repeat=7)):
  if w[0] in "2468" and int(w[-1]) % 3 != 0 and '6' in w:
    count += 1

print( count )