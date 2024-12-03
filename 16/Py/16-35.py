def F(n, m):
  if n < m:
    n, m = m, n
  if n != m:
    return F(n-m,m)
  else:
    return n

n0, m0 = 0, 0
miS = 10**9
for n in range(1, 100):
  for m in range(1, 100):
    R = F(n, m)
    if R > 15 and n != m and n+m < miS:
      n0, m0 = n, m
      miS = n + m

print( n0, m0 )

