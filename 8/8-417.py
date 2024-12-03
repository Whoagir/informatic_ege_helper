# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('ОПСТУЦШЮ', repeat = 6):
   n += 1
   s = ''.join(s)
   if s == 'ЮШОССО':
       print(n)
       break
