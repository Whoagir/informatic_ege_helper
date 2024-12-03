import sys
sys.setrecursionlimit(200)

def F(n, nest = 0):
  if nest > 100: return None
  if n <= 1: return n
  if n % 3 == 0:
    f = F(n//3 - 1, nest+1)
    return n + f if f != None else None
  else:
    f = F(n+3, nest+1)
    return n + f if f != None else None

n = 1
while True:
  r = F(n)
  if r != None:
    print( n, r )
  if r and r > 1000:
    break
  n += 1