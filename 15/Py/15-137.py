def ДЕЛ( x, d ): return x % d == 0

def F( x, A ):
  return ДЕЛ(x, A) <= (ДЕЛ(x, A) <= (ДЕЛ(x, 34) and ДЕЛ(x, 51)))

A = 1
while True:
 if all( F(x, A) for x in range(1,1000) ):
   print( A )
   break
 A += 1

