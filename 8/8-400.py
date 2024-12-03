# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('01234', repeat = 4):
    s = ''.join(s)
    if s[0] != '0' and '1' in s:
        for el in '024':
            s = s.replace(el, 'Ч')
        for el in '13':
            s = s.replace(el, 'Н')
        if 'НН' not in s and 'ЧЧ' not in s:
            k += 1
print(k)
