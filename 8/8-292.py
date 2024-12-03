from itertools import product

count = 0
glas = 'АЕИ'
for w in product( "ТИМАШЕВСК", repeat=6 ):
  w = ''.join(w)
  if sum( (c in glas) for c in w ) == 3 and \
     sum( a+'Ш' in w for a in glas ) == 0 and \
     sum( 'Ш'+a in w for a in glas ) == 0:
     # print( w )
     count += 1

print( count )