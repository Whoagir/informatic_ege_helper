from itertools import product

count = 0
for w in set(product('ЧИСТЫЙРАЗУМ', repeat=5)):
  if w.count('Й') <= 1:
    count += 1

print( count )
