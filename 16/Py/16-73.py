
m = {}
def F( n ):
  if n in m:
    return m[n]
  if n < 50:
    res = n
  else:
    res = 2*G(50 - n//2)
  m[n] = res
  return res

g = {}
def G( n ):
  if n in g:
    return g[n]
  if n > 40:
    res = 10
  else:
    res = 30 + F(n + 600//n)
  g[n] = res
  return res


print( F(80) )