from itertools import product

count = 0
glas = 'АЕИ'
for w in product( "ТИМАШЕВСК", repeat=4 ):
  w = ''.join(w)
  if sum( (c in glas) for c in w ) == 2 and \
     sum( a+'Ш' in w for a in glas ) == 0 and \
     sum( 'Ш'+a in w for a in glas ) == 0:
     # print( w )
     count += 1

print( count )


# Автор: П. Финкель

kk = 0
for a in 'ТИМАШЕВСК':
  for b in 'ТИМАШЕВСК':
    for c in 'ТИМАШЕВСК':
      for d in 'ТИМАШЕВСК':
        s = a + b + c + d
        x = s.count('А') + s.count('И') + s.count('Е')
        y = s.count('Т') + s.count('М') + s.count('Ш') + s.count('В') + s.count('С') + s.count('К')
        if x == y and ('АШ' not in s) and ('ША' not in s) \
                  and ('ИШ' not in s) and ('ШИ' not in s)\
                  and ('ЕШ' not in s) and ('ШЕ' not in s): kk += 1
print( kk )