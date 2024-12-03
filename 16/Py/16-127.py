def F( n ):
  return 2 if n < 3 else \
         2*F(n-2) - F(n-1) + 2 if n % 2 == 0 else \
         2*F(n-1) - F(n-2) - 2

print( F(17) )
