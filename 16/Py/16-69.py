
m = {}
def F( n ):
  if n in m:
    return m[n]
  if n < 4:
    res = n - 1
  elif n % 3 == 0:
    res = n + 2*F(n-1)
  else:
    res = F(n-2) + F(n-3)
  m[n] = res
  return res

print( sum( map(int, str(F(25))) ) )