
m = {}
def F( n ):
  if n in m:
    return m[n]
  if n < -100:
    res = 1
  elif n > 10:
    res = F(n-1) + 3*F(n-3) + 2
  else:
    res = - F(n-1)
  m[n] = res
  return res

print( F(20) )