def F(n):
  if n < 2: return 1
  if n % 2 == 0:
    return F(n//2) + 1
  else:
    return F(n-3) + 3

count = 0
for i in range(1, 100000):
  R = F(i)
  if R == 12:
    print( i )
    count += 1

print( "Ответ:", count )