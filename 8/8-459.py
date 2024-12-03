from itertools import product

n = 0
for w in product('0123456789ABCDE',repeat=5):
  if w[0] != '0' and w.count('8') == 1 and \
    (w.count('A') + w.count('B') + w.count('C') + w.count('D') + w.count('E') ) >= 2:
    n += 1

print( n )
