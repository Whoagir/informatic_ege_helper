# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('ДЖЗОУФЧЮЯ', repeat = 6):
   n += 1
   s = ''.join(s)
   if n % 2 != 0 and s[0] != 'У' and s[-1] != 'У':
       if 'ЮЮ' in s:
           print(n)
           break
