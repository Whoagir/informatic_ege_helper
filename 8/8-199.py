from itertools import product
A = "ABCDE"
AG = "AE"
AS = "".join(c for c in A if c not in AG)
L = 4
count = 0
for LG in range(L+1):
  w1 = [ w for w in product(AG, repeat=LG)
           if all( [p[0] <= p[1] for p in zip(w,w[1:]) ] )]
  w2 = [ w for w in product(AS, repeat=L-LG)
           if all( [p[0] >= p[1] for p in zip(w,w[1:]) ] )]
  #print( LG, L-LG )
  #print( w1 )
  #print( w2 )
  count += len(w1)*len(w2)

print(count)

# Автор: А. Куканова

from itertools import product

words = set(("".join(sorted(w)) for w in product('ABCDE', repeat=4)))
print(len(words))