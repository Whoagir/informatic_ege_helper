def F(n, nest = 0):
  if nest > 100: return None
  if n <= 5: return 1
  if n % 3 == 0:
    f1 = F(n//3 + 1, nest + 1)
    return n + f1 if f1 else None
  else:
    f1 = F(n+6, nest + 1)
    return n + f1 if f1 else None

n = 1
while True:
  r = F(n)
  if r != None and r > 1000:
    print(n, r)
    break
  n += 1