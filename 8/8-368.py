from itertools import product

def valid( s ):
  if s[0] == 0: return False
  res = False
  for k in [2,3]:
    if s[0] % k == 0:
      res, d = True, k
      for i in range(1,5):
        d = 5 - d
        res = res and s[i] % d == 0
    if res: break
  return res

count = 0
for s in product(range(15), repeat=5):
   if valid(s):
      count += 1

print( count )
