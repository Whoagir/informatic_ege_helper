def F( n ):
  return 1 if n < 3 else \
         F(n-1) + n - 1 if n % 2 == 0 else \
         F(n-2) + 2*n -2

print( F(34) )
