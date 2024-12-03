from itertools import permutations

def valid( s ):
  return s[0] not in ' У' and ' У' not in s and \
         s[-1] != ' '

count = 0
for w in set(permutations( 'ХОЧУ СОТКУ' )):
   s = ''.join( w )
   if valid( s ):
      count += 1

print( count - 1 )

# Автор: Е. Усов

from itertools import permutations as pm
b=set()
for x in pm('ХОЧУ СОТКУ'):
    s=''.join(x)
    if s[0]!='У' and s[0]!=' ' and s[-1]!=' ' and s!='ХОЧУ СОТКУ' and (s[s.index(' ')+1]!='У'):
        b.add(s)
print(len(b))

