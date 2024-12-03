def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

for p in range(13, 100):
  for q in range(14, 100):
    n1 = f( [10, 11, 12], p)
    diff = n1 - f( [11, 12, 13], q )
    if diff == 0:
      print( p, q, n1)