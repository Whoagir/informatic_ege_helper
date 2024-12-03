def F(n):
  if n == 1: return 1
  if n % 2 == 0:
    return F(n//2) + 1
  else:
    return F(n-1) + n

for i in range(1, 100000):
  R = F(i)
  if R == 19:
    print( i )
    break
