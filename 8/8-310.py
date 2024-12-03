from itertools import permutations

Glas = 'АИ'
count = 0
for w in set(permutations('АМФИБРАХИЙ')):
   i = w.index('Ф')
   if i > 1 and i+2 < len(w) and \
      w[i-1] in Glas and w[i-1] == w[i-2] and \
      w[i+1] in Glas and w[i+1] == w[i+2]:
      count += 1
print( count )


