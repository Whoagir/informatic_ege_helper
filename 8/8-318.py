from itertools import product

def valid( s ):
  if s[0] == '0' or \
     any( s[0]>=s[i] or s[1]>=s[i]
          for i in range(2,6) ):
    return False
  s = ''.join( c if int(c) % 2 == 1 else '.'
               for c in s )
  return '...' not in s

count = 0
for w in product( '01234567', repeat=6 ):
   s = ''.join( w )
   if valid( s ):
      count += 1

print( count )

# Автор: А. Бриккер

from itertools import *
k = 0
for x in product('01234567', repeat=6):
    s = ''.join(x)
    if int(s[0]):
        if max(s[:2]) < min(s[2:]):
            for el in '0246':
                s = s.replace(el, '*')
            if '***' not in s:
                k += 1
print(k)

