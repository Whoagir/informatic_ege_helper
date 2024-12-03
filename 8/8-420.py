# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('МОТЮ', repeat = 5):
   n += 1
   s = ''.join(s)
   if s[0] == 'О':
       print(n)
