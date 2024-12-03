def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

from itertools import product

for p in range(99, 4, -1):
  print( p )
  for q in range(99, 4, -1):
    r = min(p, q, 10)
    for a, b, c in product(range(r), repeat=3):
      if a*b > 0 and len({a,b,c}) == 3:
        n1 = f([a, b, c, 1], p)
        n2 = f([b, c, 1, 0], q)
        d = n1 - n2
        if 0 <= d < min(q,10) and d not in {a,b,c}:
          print( p, q, a, b, c, d )
          print( f([a, b, c, 1], p), f([b, c, 1, d], q) )