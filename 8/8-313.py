from itertools import permutations

count = 0
for w in set(permutations('АМФИБРАХИЙ')):
   w = ''.join(w)
   if any( ai in w for ai in ['АА', 'АИ', 'ИА', 'ИИ'] ):
      count += 1
print( count )


