def F( n ):
  return 1 if n < 3 else \
         F(n-2) - F(n-1) if n % 2 == 0 else \
         F(n-2) - F(n-3)

print( F(50) )
