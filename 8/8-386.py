from itertools import permutations

count = 0
for w in set(permutations('НОСОЧЕЧКИ')):
  w = ''.join(w)
  [ w := w.replace(c,'g') for c in 'ОЕИ' ]
  [ w := w.replace(c,'s') for c in 'НСЧК' ]
  if 'gg' not in w and 'ss' not in w:
    count += 1

print( count )
