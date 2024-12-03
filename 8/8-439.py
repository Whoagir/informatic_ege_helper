# Автор: М. Ишимов

from itertools import *
n = 0
for s in product('БНПЭ', repeat = 4):
   n += 1
   s = ''.join(s)
   if n % 2 == 0 and s[0] != 'П' and s[-1] != 'П':
       if 'ЭЭ' not in s:
           print(n)
