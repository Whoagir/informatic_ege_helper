def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

from itertools import product
p = 7
found = False
while not found:
  for x, y in product(range(p), repeat=2):
    if f([1,6,1],p)*f([5,6],p) == f([5,x,y,6],p):
      print( p, x, y, f([y,x],p) )
      found = True
      break
  p += 1
