def F(n):
  if n < 2: return 1
  if n % 3 == 0:
    return F(n//3) - 1
  else:
    return F(n-1) + 17

for i in range(1, 100000):
  R = F(i)
  if R == 110:
    print( i )
    break
