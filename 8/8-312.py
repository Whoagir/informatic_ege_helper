from itertools import permutations

Sogl = 'МФБРХ'
count = 0
for w in set(permutations('АМФИБРАХИЙ')):
   if all( c in Sogl for c in w[1::2] ):
      count += 1
print( count )


