import sys
sys.setrecursionlimit(100)

def F(n):
  if n <= 5: return 1
  if n % 4 == 0:
    return n + F(n//2 - 1)
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
    if r > 1000:
      break
  n += 1