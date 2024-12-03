from itertools import product

count = 0
for w in set(product('КРЕМНИЙ', repeat=5)):
  w = ''.join(w)
  if w.count('Й') <= 2:
    [ w := w.replace(c,'s') for c in 'КРМНЙ' ]
    [ w := w.replace(c,'g') for c in 'ЕИ' ]
    if w.count('g') > 0 and w.count('g') % 2 == 0:
      count += 1

print( count )
