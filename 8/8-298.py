from itertools import product

count = 0
for n in product( '01234', repeat=5 ):
  n = ''.join(n)
  if n[0] != '0' and \
     all( abs(int(p[0])-int(p[1])) >= 2
          for p in zip(n, n[1:]) ) :
     count += 1

print( count )

# Автор: М. Ишимов
def pr(x): return all(x % d != 0 for d in range(2, int(x**0.5) + 1))
s = [c for c in range(5)]
from itertools import *
res = 0
for x in product(s, repeat=5):
    if x[0] != 0:
        if all(abs(x[i-1]-x[i]) >= 2 and abs(x[i]-x[i+1]) >= 2 for i in range(1, 4)):
            res += 1
print(res)

