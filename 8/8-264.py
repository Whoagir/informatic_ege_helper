from itertools import product

A = "ГЕКЭ023"

for i, w in enumerate(product(A, repeat = 4)):
  w = "".join(w)
  if w[0] in "023" and \
     all( ch+ch not in w for ch in A ):
    break

print( i+1 )