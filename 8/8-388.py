from itertools import permutations

count = 0
for w in permutations('ВЕБИНАР'):
  w = ''.join(w)
  [ w := w.replace(c,'g') for c in 'ЕИА' ]
  [ w := w.replace(c,'s') for c in 'ВБНР' ]
  if 'gg' not in w and 'ss' not in w:
    count += 1

print( count )
