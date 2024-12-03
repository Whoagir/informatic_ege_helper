def D( x, d ): return x % d == 0
def nD( x, d ): return x % d != 0
def f( x, A):
  return (D(x, 2) <= nD(x, 3)) or (x + A >= 80)

from itertools import product
for A in range(1,10000):
  if all( f(x, A) for x in range(1,1000) ):
    print(A)
    break
