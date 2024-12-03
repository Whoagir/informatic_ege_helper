from itertools import product

count = 0
for w in set(product('ЕИЙКНОТ', repeat=7)):
  if 'КОТ' in ''.join(w):
    count += 1

print( count )
