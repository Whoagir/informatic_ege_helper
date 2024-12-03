def F(n):
  if n < 2: return n
  if n % 2 == 0:
    return F(n//2) + 1
  else:
    return F(3*n+1) + 1

count = 0
for i in range(1, 101):
  R = F(i)
  print( i, R )
  if R > 100:
    count += 1

print( "Ответ:", count )