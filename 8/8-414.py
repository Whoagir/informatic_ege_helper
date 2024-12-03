# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('0123456789', repeat = 4):
    s = ''.join(s)
    if s[0] != '0' and s.count('8') <= 2:
        for el in '13579':
            s = s.replace(el, 'Н')
        if '8Н' not in s and 'Н8' not in s:
            k += 1
print(k)
