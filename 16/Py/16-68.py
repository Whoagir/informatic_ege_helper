
m = {}
def F( n ):
  if n in m:
    return m[n]
  if n < 3:
    res = n + 1
  elif n % 2 == 0:
    res = F(n-2) + n - 2
  else:
    res = F(n+2) + n + 2
  m[n] = res
  return res

cnt = 0
for x in range(2, 100000,2):
  if len(str(F(x))) == 5:
    if x < 1000:
      print(x)
    cnt += 1

print( cnt )