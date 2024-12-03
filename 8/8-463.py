from itertools import product

digits = '0123456789'
letters = 'ABCD'
A = digits + letters
N = 8

if N <= 5:
  count = 0
  for w in product(A, repeat=N):
    if w[0] != '0' and w.count('0') == 2 and \
       sum( c in letters for c in w) <= 4:
      count += 1
  print( count )

from functools import lru_cache
@lru_cache
def f( L, n0, nA ):
  if L == 0:
    return (n0 == 2 and nA <= 4)
  count = f(L-1, n0+1, nA) if n0 < 2 else 0
  for nxt in digits[1:]:
    count += f(L-1, n0, nA)
  if nA < 4:
    for nxt in letters:
      count += f(L-1, n0, nA+1)
  return count

count = 0
for first in A[1:]:
  count += f(N-1, 0, int(first > '9'))

print( count )
