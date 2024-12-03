import sys
sys.setrecursionlimit(100)

def F(n):
  if n <= 5: return n
  if n % 3 == 0:
    return n + F(n//3 + 2)
  else:
    return n + F(n+6)

n = 1
while True:
  try:
    r = F(n)
  except:
    pass
  else:
    print(n, r)
    if r > 1000:
      break
  n += 1