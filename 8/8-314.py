from itertools import product

def valid( w ):
  return all( s not in w
              for s in ['ЕЕ', 'ЯЯ', 'ЯЕ',  'ЕЯ',
                        'ЛС', 'ЛЛ', 'СЛ',  'СС' ] )
count = 0
for w in product( 'ЛЕСЯ', repeat=4 ):
   w = ''.join( w )
   for k in range(1,4):
     s = w[:k] + ' ' + w[k:]
     if valid( s ):
        count += 1

print( count )

# Автор: Е. Усов

from itertools import product as pr
count=0
for x in pr(' ЛЕСЯ',repeat=5):
    s=''.join(x)
    if s[0]!=' ' and s[-1]!=' ' and 'ЛС' not in s and 'СЛ' not in s and 'ЛЛ' not in s\
            and 'СС' not in s and 'ЕЯ' not in s and 'ЯЕ' not in s and 'ЕЕ' not in s \
            and 'ЯЯ' not in s and s.count(' ')==1:
        count+=1
print(count)
