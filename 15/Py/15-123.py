def D(a, b): return a % b == 0
def nD(a, b): return a % b != 0
def f( x, A ):
  return D(x,18) <= ( nD(x,A)  <=  nD(x,12) )

for A in range(1, 1000):
   OK = True
   for x in range(1,1000):
      if not f(x, A):
        OK = False
        break
   if OK:
     print( A )