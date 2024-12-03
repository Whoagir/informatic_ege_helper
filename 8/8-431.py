# Автор: М. Ишимов

from itertools import *
n = ans = 0
for s in product('ВЕЛНРХ', repeat = 5):
   n += 1
   s = ''.join(s)
   if n % 2 != 0 and s[:2] == 'ЕН':
       ans += 1
print(ans)
