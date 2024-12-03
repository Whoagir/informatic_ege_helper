
def F( n ):
  if n <= 3:
    return n
  if n % 2 == 0:
    return 2*n + F(n-1)
  else:
    return n*n + F(n-2)

cnt = 0
for x in range(1, 101):
  if F(x) % 3 == 0:
    cnt += 1

print( cnt )