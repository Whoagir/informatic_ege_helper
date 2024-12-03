def F( n ):
  if n == 0: return 0
  if n % 2 == 0:
    return F(n // 2) + 3
  else:
    return 2*F(n-1) + 1

count = 0
f = set()
for n in range(1,1000+1):
  f.add( F(n) )

print( len(f) )
