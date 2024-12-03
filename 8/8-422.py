# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('БВЕКЛОУФ', repeat = 5):
   n += 1
   s = ''.join(s)
   if s[0] + s[-1] == 'ФЛ':
       print(n)
       break
