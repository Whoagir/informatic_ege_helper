def D(x, d): return x % d == 0
def nD(x, d): return x % d != 0
def f(x, A):
  return D(x, 33) <= (nD(x, A) <= nD(x, 242))

for A in range(1000, 0, -1):
  if all( f(x,A) for x in range(1,10000) ):
    print( A )
    break

