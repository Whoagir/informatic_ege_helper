from itertools import product

count = 0
for w in set(product('ВАСЯ', repeat=5)):
  if w.count('А') >= 1:
    count += 1

print( count )
