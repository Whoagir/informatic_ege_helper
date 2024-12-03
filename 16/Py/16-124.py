from functools import cache

@cache
def F( n ):
  return 1 if n < 3 else \
         G(n) + F(n-1) if n % 2 == 0 else \
         F(n-2) - 2*G(n+1)
@cache
def G( n ):
  return 1 if n < 3 else \
         F(n-3) + F(n-2) if n % 2 == 0 else \
         F(n+1) - G(n-1)

print( G(120) )