def F( n ):
  return n-10000 if n > 10000 else \
         F(n+1) + F(n+2)

print( F(12345)*1 + F(10101) )
