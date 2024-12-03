def D( x, d ): return x % d == 0
def nD( x, d ): return x % d != 0

def f(x, A):
   return (D(x,175) <= nD(x,25)) or (2*x+A >=1780)

for A in range(1,10000):
   if all( f(x,A) for x in range(1,100000) ):
      print(A)
      break
