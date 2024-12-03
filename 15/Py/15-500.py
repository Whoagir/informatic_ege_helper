def D( x, d ): return x % d == 0
def nD( x, d ): return x % d != 0

def f(x, A):
   return (D(x,7) <= nD(x,21)) or (2*x+A >=120)

for A in range(1,1000):
   if all( f(x,A) for x in range(1,10000) ):
      print(A)
      break
