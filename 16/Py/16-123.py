from math import log

def trinary( n ):
  s = ''
  while n:
    s = str(n%3) + s
    n //= 3
  return s

MAX = 100_000_000
Lmax = int(log(MAX,3)) + 1

count = 0
def rec( s, n0, L ):
  global count
  if n0 == 0 and len(s) == L and int(s,3) < MAX:
    #print( s, int(s,3) )
    count += 1
  if len(s) > L: return
  rec( s + '1', n0, L )
  rec( s + '2', n0, L )
  if n0 > 0:
    rec( s + '0', n0-1, L )

for L in range(Lmax,1,-1):
  rec( '1', 2, L )
  rec( '2', 2, L )

print(count)

"""
count = 0
for n in range (MAX):
   s = trinary(n)
   if s.count('0') == 2:
      count += 1
print(count)

from functools import lru_cache

@lru_cache
def f( n ):
  return 8 if n == 0 else \
         5+f(n//3) if n % 3 == 0 else \
         f(n//3)

count = 0
for i in range(MAX):
  if f(i) == 18:
    #print(i, trinary(i))
    count += 1
print( count )
"""
