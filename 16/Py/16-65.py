
def F( n ):
  if n <= 5:
    return n + 15
  if n % 2 == 0:
    return F(n // 2) + n**3 - 1
  else:
    return F(n-1) + 2*n*n + 1

cnt = 0
for x in range(1, 1000+1):
  s = str(F(x))
  if s.count('8') >= 2:
    cnt += 1
    print(cnt, x)

print( cnt )