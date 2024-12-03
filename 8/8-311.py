from itertools import permutations

count = 0
for w in set(permutations('АМФИБРАХИЙ')):
   w = ''.join(w)
   i = w.find('БР')
   if i == 4:
      count += 1
print( count )


