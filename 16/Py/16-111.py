def F(n):
  if n <= 0: return 0
  if n % 2 == 0: return F(n//2) - 2
  return 2 + F(n-1)

count = {}
for n in range(1000):
  f = F(n)
  count[f] = count.get(f,0) + 1

print( count )