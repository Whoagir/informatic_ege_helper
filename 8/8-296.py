from itertools import product

def isPrime( n  ):
  return n > 1 and all( n % d != 0 for d in range(2,round(n**0.5)+1) )

count = 0
for n in product( '0123456', repeat=5 ):
  n = ''.join(n)
  s = sum( map(int, n) )
  nEven = sum( d in '0246' for d in n )
  if n[0] != '0' and nEven >= 3 and isPrime(s):
     count += 1

print( count )


# Автор: М. Ишимов
def pr(x): return x > 1 and all(False for d in range(2, int(x**0.5) + 1) if x % d == 0)
s = '0123456'
from itertools import *
res = 0
for x in product(s, repeat=5):
    if x[0] != '0' and sum(x.count(c) for c in '0246') >= 3:
        if pr( sum(map(int, x)) ): res += 1
print(res)
