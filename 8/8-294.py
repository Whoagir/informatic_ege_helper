from itertools import product

count = 0
glas = 'АЕИ'
sogl = 'ТМШВСК'

count = 0
for w in product( sorted("ТИМАШЕВСК", reverse=True), repeat=5 ):
  count += 1
  w = ''.join(w)
  if w == w[::-1] and w[2] in sogl and \
     sum( c in sogl for c in w ) == 1:
     print( count, w )
     break

