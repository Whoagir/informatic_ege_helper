# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('АДИУХШ', repeat = 6):
   n += 1
   s = ''.join(s)
   if n % 2 != 0 and s[0] != 'А':
       if s.count('Ш') <= 3 and 'Х' not in s:
           print(n)
           break
