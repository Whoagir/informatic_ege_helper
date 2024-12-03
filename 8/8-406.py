# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('0123456789AB', repeat = 5):
    s = ''.join(s)
    if s[0] != '0' and s.count('4') == 2:
        for el in '13579B':
            s = s.replace(el, 'Н')
        if '4Н' not in s and 'Н4' not in s:
            k += 1
print(k)
