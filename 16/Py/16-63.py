def F( n ):
  if n <= 13:
    return n**3 + n**2 + 1
  if n % 3 == 0:
    return F(n-1) + 2*n**2 - 3
  else:
    return F(n-2) + 3*n + 6

def valid( y ):
  s = str(y)
  for c in s:
    if c in '02468':
      return False
  return True

cnt = 0
for x in range(1, 1000+1):
  if valid(F(x)):
    cnt += 1

print( cnt )