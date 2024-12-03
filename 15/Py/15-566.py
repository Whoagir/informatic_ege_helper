def D(x, d): return x % d == 0
def nD(x, d): return x % d != 0
def f(x, A):
  return D(x,A) or ((70 <= x <= 90) <= nD(x,22))

for A in range(1000, 0, -1):
  if all( f(x,A) for x in range(1,10000) ):
    print( A )
    break

