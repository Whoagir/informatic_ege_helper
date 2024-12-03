def F(n):
  if n <= 2 or n == 8:
    return 0
  if n == 3: return 1
  return F(n-2)+F(n-1)

n = 1
while F(n) != 25:
  n += 1

print(n)