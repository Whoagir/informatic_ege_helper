def F( n ):
  return n*3 if n < 3 else \
         (F(n-2)*F(n-1) - n) % 100 if n % 2 == 0 else \
         (F(n-1) - F(n-2) + 2*n) % 100

print( F(30) % 100 )
