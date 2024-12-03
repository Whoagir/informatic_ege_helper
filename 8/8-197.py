from itertools import product
A = "КСЕНИЯ"
AG = "ЕИЯ"
s = 0
for L in range(3, 8):
  words = [ w for w in product(AG, repeat=L)
            if all( [w.count(c) <= 2 for c in AG ] )]
  print(L, len(words) )
  s += len(words)
  words = [ w for w in product(AG, repeat=L-1)
              if all( [w.count(c) <= 2 for c in AG ] )]
  print(L, 3*len(words) )
  s += 3*len(words)

print(s)