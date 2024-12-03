from itertools import product

count = 0
for w in product(sorted(set('ЕПСУХ')), repeat=5):
  s = ''.join(w)
  if s[-1] in 'ПСХ':
    count += 1
    if s == 'УСПЕХ':
      print( count )
