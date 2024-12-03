
m = {}
def F( n ):
  if n in m:
    return m[n]
  if n == 0:
    res = 1
  elif n > 0:
    res = 2*F(1-n) + 3*F(n-1) + 2
  else:
    res = -F(-n)
  m[n] = res
  return res

print( sum( map(int, str(F(50))) ) )