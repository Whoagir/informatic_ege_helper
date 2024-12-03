def F( n ):
  if n > 20:
    return n**3 + n
  if n % 2 == 0:
    return 3*F(n+1) + F(n+3)
  else:
    return F(n+2) + 2*F(n+3)

def valid( y ):
  s = str(y)
  return not '1' in s

cnt = 0
for x in range(1, 1000+1):
  if valid(F(x)):
    cnt += 1

print( cnt )