def F( n ):
  return n if n < 2 else \
         F(n//2) + 1 if n % 2 == 0 else \
         F(3*n+1) + 1

count = 0
for i in range(1, 100000):
  if F(i) == 16:
    count += 1

print( count )
