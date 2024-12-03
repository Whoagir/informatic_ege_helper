import sys

sys.setrecursionlimit( 10000 )

M = [None]*11000
def F( n ):
  if n <= 10: return n
  if n > 10000: return 1
  if M[n] is not None: return M[n]
  M[n] = n % 10 + F(n+2) if n % 2 == 0 else \
         F(n-2) - (n-1) % 10
  return M[n]

print( F(4500) + F(5515) )


