def F( n ):
  if n == 0: return 0
  if n % 2 == 0:
    return F(n // 2)
  else:
    return F(n-1) + 3

count = 0
f = []
for n in range(1,1000+1):
  f.append( F(n) )
  if F(n) == 18:
    count += 1

from collections import Counter

print( count )
print( Counter(f) )