from itertools import permutations

A = "ЛЕБНЫЙМЯКИШ"
S = "ХЛБНЙМКШ"

count = 0
for w in permutations(A, 6):
  w = 'Х' + ''.join(w)
  if w[3] in 'БЫКИШ' and \
     all( not (a in S and b in S) for a, b in zip(w, w[1:]) ):
    count += 1

print( count )

