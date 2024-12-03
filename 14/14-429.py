def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

for p in range(100, 1000):
  q = int(str(p)[::-1])
  if f([9,6,1], p) == f([1,6,9], q):
    print( p, q )