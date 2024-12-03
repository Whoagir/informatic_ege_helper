# Автор: М. Ишимов

from itertools import *
n = ans = 0
for s in product('БЕЧЮ', repeat = 5):
   n += 1
   s = ''.join(s)
   if n % 2 == 0 and s[0] != 'Ю' and 'ЕЕ' not in s:
       ans += 1
print(ans)
