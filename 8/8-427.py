# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('ГЕНОСТХЮ', repeat = 4):
   n += 1
   s = ''.join(s)
   if n % 2 != 0 and s[0] != 'Н':
       if s.count('О') >= 2 and 'С' not in s:
           print(n)
