from itertools import product

count = 0
glasv = 'АЕИВ'
for w in product( "ТИМАШЕВСК", repeat=5 ):
  w = ''.join(w)
  if sum( a+'Ш' in w for a in glasv ) == 0 and \
     sum( 'Ш'+a in w for a in glasv ) == 0:
     count += 1

print( count )

