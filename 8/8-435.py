# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('БДЕКНТЦЧЭ', repeat = 6):
   n += 1
   s = ''.join(s)
   if n % 2 == 0 and s[0] != 'Н' and s[-1] != 'Н':
       if s.count('Е') >= 3:
           print(n)
           break
