def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

for p in range(1, 100):
  for q in range(p+1, 100):
    if f([2,4,3,5,1], p) == f([1,4, 3, 2, 5], q):
      print( p, q, f([2,4,3,5,1], p) )
      break