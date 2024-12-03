def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

from itertools import product

for x in range(68):
  n = f( [1, 2, 3, x, 5], 68 ) + \
      f( [1, x, 2, 3, 3], 68 )
  if n % 12 == 0:
    print( x, n // 12)