
def F( n ):
  return f"{n:b}".count('1')

from math import factorial

def Cnk( n, k ):
  return factorial(n)//factorial(n-k)//factorial(k)

count = Cnk( 30, 3 )

print( count )
