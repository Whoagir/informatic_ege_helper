# Автор: М. Ишимов

from itertools import *
n = ans = 0
for s in product('БВМНОУШЩ', repeat = 4):
   n += 1
   s = ''.join(s)
   if n % 2 != 0 and s[-1] != 'В':
       ans += 1
print(ans)
