from itertools import product

count = 0
for w in set(product('ПРИКАЗ', repeat=4)):
  if w.count('К') == 1:
    count += 1

print( count )
