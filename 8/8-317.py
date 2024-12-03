from itertools import product

glas = 'АЕО'
def valid( s ):
  indGlas = [ i for i, c in enumerate(s)
                  if c in glas ]
  return len(indGlas) >= 2 and \
         all( j-i > 1 for i, j in zip(indGlas, indGlas[1:]) )

count = 0
for w in product( 'КОНФЕТА', repeat=5 ):
   s = ''.join( w )
   if valid( s ):
      count += 1

print( count )

# Автор: А. Бриккер

from itertools import *
k = 0
for x in product('КОНФЕТА', repeat=5):
    s = ''.join(x)
    if sum(s.count(c) for c in 'ОЕА') > 1:
        for el in 'КНФТ':
            s = s.replace(el, '*')
        if all( '*' in s[i + 1: j]
                for i in range(len(s) - 1)
                    for j in range(i + 1, len(s))
                        if '*' not in [s[i], s[j]] ):
            k += 1
print(k)
