# Автор: М. Ишимов

from itertools import *
n = ans = 0
for s in product('ГЕЗНОПСТЮ', repeat = 6):
   n += 1
   s = ''.join(s)
   if n % 2 != 0 and s[0] != 'С' and s.count('Т') <= 1:
       ans += 1
print(ans)
