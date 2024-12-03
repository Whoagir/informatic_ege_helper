from itertools import product

count = 0
for n in product( '012345678', repeat=6 ):
  n = ''.join(n)
  s = sum( map(int, n) )
  nOdd = sum( (d in '1357') for d in n )
  if n[0] != '0' and nOdd <= 2 and s % 6 == 0 and s % 4 != 0:
     count += 1

print( count )


# Автор: М. Ишимов
s = '012345678'
from itertools import *
res = 0
for x in product(s, repeat=6):
    if x[0] != '0' and sum(x.count(c) for c in '1357') <= 2:
        if sum(map(int, x)) % 4 != 0 and sum(map(int, x)) % 6 == 0: res += 1
print(res)
