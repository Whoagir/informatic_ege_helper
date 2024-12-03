from itertools import permutations

count = 0
for w in set(permutations('ПРОБНИК')):
  w = ''.join(w)
  [ w := w.replace(c,'s') for c in 'ПРБНК' ]
  [ w := w.replace(c,'g') for c in 'ОИ' ]
  if w[0] == 's' and w[-1] == 's' and 'gg' not in w:
    count += 1

print( count )
