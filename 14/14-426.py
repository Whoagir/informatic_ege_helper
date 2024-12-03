def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

for p in range(1000, 10000):
  q = int(str(p)[::-1])
  if f([4,4,1], p) == f([1,4,4], q):
    print( p, q )