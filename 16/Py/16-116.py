def F( n ):
  return 1 if n <= 1 else \
         11*n + F(n-1) if n > 1 and n % 2 == 0 else \
         11*F(n-2) + n;

s = 0
for i in range(35,50+1):
  val = F(i)
  if val % 2 == 0:
    s += val

print( len(str(s)) )