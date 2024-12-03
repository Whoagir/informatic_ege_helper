def F( n ):
  return n if n >= 2020 else \
         n + 2 + F(n+3)

print( F(2012) - F(2023) )
