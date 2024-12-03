# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('ГЖИМФЧЯ', repeat = 6):
   n += 1
   s = ''.join(s)
   if s[0] + s[1] == 'ЖЯ':
       print(n)
       break
