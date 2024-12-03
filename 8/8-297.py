from itertools import product

def isPrime( n  ):
  return n > 1 and all( n % d != 0 for d in range(2,round(n**0.5)+1) )

count = 0
for n in product( '01234567', repeat=5 ):
  n = ''.join(n)
  if n[0] != '0' and \
     any( p[0] != p[1] and isPrime(int(p[0])+int(p[1])) for p in product(n, repeat=2) ):
     count += 1

print( count )

# Автор: М. Ишимов
def pr(x): return x > 1 and all(False for d in range(2, int(x**0.5) + 1) if x % d == 0)
s = '01234567'
from itertools import *
res = 0
for x in product(s, repeat=5):
    if x[0] != '0':
        m = [pr( int(x[i]) + int(x[j])) for i in range(5) for j in range(5) if x[i] != x[j]]
        if any(m): res += 1
print(res)
