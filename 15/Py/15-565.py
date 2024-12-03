def D(x, d): return x % d == 0
def nD(x, d): return x % d != 0
def f(x, A):
  return (D(x,2) <= nD(x,5)) or (x + A >= 70)

for A in range(1,10000):
  if all( f(x,A) for x in range(1,10000) ):
    print( A )
    break

for A in range(1, 1000):
  flag = 1
  for x in range(1, 10000):
    F = ((x % 2 == 0) <= (x % 5 != 0)) or (x + A >= 70)
    if not F:
      flag = 0
      break
  if flag == 1:
    print(A)
    break