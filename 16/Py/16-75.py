def F(n):
  if n <= 1: return 1
  if n % 2 == 0:
    return 1 + F(n//2)
  else:
    return 1 + F(n+2)

n = 1
while True:
  try:
    r = F(n)
  except:
    pass
  else:
    print(n, F(n))
  n += 1