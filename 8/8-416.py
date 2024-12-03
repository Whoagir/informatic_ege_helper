# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('КХНЭШЧФЖ', repeat = 8):
   s = ''.join(s)
   if s.count('Ш') <= 1:
       k += 1
print(k)
