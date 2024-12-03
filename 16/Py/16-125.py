from functools import lru_cache
def sumDigits( n ):
  return sum( map(int, str(n)) )

@lru_cache
def F( n ):
  return 1 if n < 3 else \
         F(n-1) - F(n-2) if sumDigits(n) % 2 == 0 else\
         F(n-1) + F(n//2)

print( F(100) )