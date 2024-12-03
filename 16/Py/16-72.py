
def F( n ):
  if n <= 70:
    res = F(n+2) + 2*F(3*n)
  else:
    res = n - 50
  return res

print( F(40) )