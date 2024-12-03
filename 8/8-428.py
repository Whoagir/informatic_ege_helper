# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('АМНФ', repeat = 4):
   n += 1
   s = ''.join(s)
   if n % 2 == 0 and s[0] != 'А':
       if s.count('Н') >= 2 and 'Ф' not in s:
           print(n)
           break
