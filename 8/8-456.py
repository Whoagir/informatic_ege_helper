from itertools import product

count = 0
for w in product('01234567',repeat=5):
  if w[0] not in '01357' and w[-1] not in '26' and \
     w.count('7') <= 2:
    count += 1

print ( count )
