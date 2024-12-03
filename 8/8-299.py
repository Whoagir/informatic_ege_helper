from itertools import product

def isPalindrom( n ):
  return n == n[::-1]

count = 0
for n in product( '01234567', repeat=6 ):
  n = ''.join(n)
  if n[0] != '0' and isPalindrom(n) and \
     sum( int(d) for d in n if d in '0246' )  \
       <= sum( int(d) for d in n if d in '1357' ):
     count += 1

print( count )

s = '01234567'
from itertools import *
res = 0
for x in product(s, repeat=6):
    if x[0] != '0':
        if sum(int(c) for c in x if c in '0246') <= sum(int(c) for c in x if c in '1357'):
            if x == x[::-1]: res += 1
print(res)