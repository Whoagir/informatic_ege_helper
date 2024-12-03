def F( n ):
  return n*n + 4*n + 3 if n > 25 else \
		 F(n+1) + 2*F(n+4) if n % 3 == 0 else \
		 F(n+2) + 3*F(n+5);

def valid( y ):
  s = sum( map(int, str(y)) )
  return s == 24

cnt = 0
for x in range(1, 1000+1):
  if valid(F(x)):
    cnt += 1

print( cnt )