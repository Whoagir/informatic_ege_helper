
m = {}
def F( n ):
  if n in m:
    return m[n]
  if n < 3:
    res = n + 1
  elif n % 2 == 0:
    res = n + 2*F(n + 2)
  else:
    res = F(n-2) + n - 2
  m[n] = res
  return res

cnt = 0
for x in range(1, 1000000,2):
  if len(str(F(x))) == 3:
    cnt += 1

print( cnt )