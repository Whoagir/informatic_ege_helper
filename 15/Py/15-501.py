def D( x, d ): return x % d == 0
def nD( x, d ): return x % d != 0

def f(x, A):
   return (D(x,12) <= nD(x,90)) or (x+2*A >=512)

for A in range(1,1000):
   if all( f(x,A) for x in range(1,100000) ):
      print(A)
      break
