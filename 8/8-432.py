# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('ЕКМОСЧ', repeat = 4):
   n += 1
   s = ''.join(s)
   if n % 2 == 0:
       if s[0] == 'Ч' and s[-1] == 'О':
           print(n)
