def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

from itertools import product

p = 9
found = False
while not found:
  for x, y in product(range(p), repeat=2):
    if f([7,5],p)*f([8,7],p) == f([1,x,y,2],p):
      print( p, x, y, f([y,x],p) )
      found = True
      break
  p += 1
