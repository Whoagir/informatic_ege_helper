from itertools import product

count = 0
glas = 'АЕИ'
sogl = 'ТМШВСК'

for w in product( "ТИМАШЕВСК", repeat=6 ):
  w = ''.join(w)
  if sum( (c in glas) for c in w ) < 3 and \
     sum( a+'Ш' in w for a in sogl ) == 0 and \
     sum( 'Ш'+a in w for a in sogl ) == 0:
     # print( w )
     count += 1

print( count )


# Автор: П. Финкель

from itertools import *
k = 0
for s in product('ТИМАШЕВСК',repeat=6):
  s = ''.join(s)
  x = s.count('А') + s.count('И') + s.count('Е')
  y = s.count('Т') + s.count('М') + s.count('Ш') + s.count('В') + s.count('С') + s.count('К')
  if x < y and 'ТШ' not in s and 'ШТ' not in s and \
               'МШ' not in s and 'ШМ' not in s and \
               'ВШ' not in s and 'ШВ' not in s and \
               'СШ' not in s and 'ШС' not in s and \
               'КШ' not in s and 'ШК' not in s and 'ШШ' not in s:
    k += 1

print( k )
