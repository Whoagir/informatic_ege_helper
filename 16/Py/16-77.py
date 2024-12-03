import sys
sys.setrecursionlimit(100)

def F(n):
  if n <= 1: return 1
  if n % 3 == 0:
    return n + F(n//3)
  else:
    return n + F(n+3)

n = 1
while True:
  try:
    r = F(n)
  except:
    pass
  else:
    print(n, r)
    if r >= 100:
      break
  n += 1