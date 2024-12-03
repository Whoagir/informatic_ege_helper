from itertools import product

for i, w in enumerate( sorted(product( set('МАРИНА'), repeat=8)) ):
  if ''.join(w) == 'МАРИАННА':
    print( i+1 )
    break

# 01234  20410330
# АИМНР  МАРИАННА
print( int('20410330',5)+1 )