from itertools import product

n = 0
for w in product('0123456789ABCD',repeat=5):
  if w[0] != '0' and w.count('9') == 1 and \
    (w.count('B') + w.count('C') + w.count('D') ) <= 3:
    n += 1

print( n )
