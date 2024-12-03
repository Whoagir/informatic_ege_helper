import sys
sys.setrecursionlimit(100)

def F(n):
  if n <= 1: return 1
  if n % 2 == 0:
    return 3 + F(n//2 - 1)
  else:
    return n + F(n+2)

n = 1
while True:
  try:
    r = F(n)
  except:
    pass
  else:
    print(n, r)
    if r == 19:
      break
  n += 1