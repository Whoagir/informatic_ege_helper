from itertools import permutations

ov = "abde"

count = 0
for w in permutations( 'abcdef', 4 ):
   w = ''.join( w )
   for c in ov:
     w = w.replace( c, '.' )
   if '..' not in w:
     count += 1

print( count )