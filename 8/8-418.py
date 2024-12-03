# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('АДКУФХЯ', repeat = 6):
   n += 1
   s = ''.join(s)
   if s[0] == 'Х':
       print(n)
       break
