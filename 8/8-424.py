# Автор: М. Ишимов

from itertools import *
n = ans = 0
for s in product('АДЗМНРЧЮЯ', repeat = 5):
   n += 1
   s = ''.join(s)
   if n % 2 != 0 and s[0] == 'А' and s.count('Ю') == 2:
       ans += 1
print(ans)
