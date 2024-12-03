def K( a, b ): return a & b == 0
def nK( a, b ): return a & b != 0

def f(x, A):
  return ( nK(x,112) or nK(x,86) ) <= ( K(x,65) <= nK(x,A) )

allA = [ A for A in range(1,1000)
           if all( f(x,A) for x in range(1,1000) ) ]

print( min(allA) )