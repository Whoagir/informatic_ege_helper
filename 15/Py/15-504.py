def D(x, d): return x % d == 0
def nD(x, d): return x % d != 0

def f(x, A):
  return (D(x, 6) <= nD(x, 14)) or (x + A >= 70) and D(A, 20)

A = 1
while True:
  if all( f(x,A) for x in range(1,100000) ):
    print( A )
    break
  A += 1

