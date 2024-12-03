
m = {}
def F( n ):
  if n in m:
    return m[n]
  if n == 0:
    res = 5
  elif n > 0:
    res = 3*F(n-4)
  else:
    res = F(n+3)
  m[n] = res
  return res

print( F(43) )