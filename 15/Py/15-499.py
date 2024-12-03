def D( x, d ):
  return x % d == 0

def f(x, A):
   return (D(x,3) <= (not D(x,5))) or (x+A >=70)

for A in range(1,1000):
   if all( f(x,A) for x in range(1,1000) ):
      print(A)
      break
