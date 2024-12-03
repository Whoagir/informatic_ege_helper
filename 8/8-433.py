# Автор: М. Ишимов

from itertools import *
n = ans = 0
for s in product('ГДИМОТХЩЭ', repeat = 5):
   n += 1
   s = ''.join(s)
   if n % 2 == 0 and s[0] not in 'МИ':
       ans += 1
print(ans)
