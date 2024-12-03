# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('0123456789', repeat = 6):
    s = ''.join(s)
    if s[0] != '0' and s.count('4') <= 1:
        for el in '02468':
            s = s.replace(el, 'Ч')
        for el in '13579':
            s = s.replace(el, 'Н')
        if 'НН' not in s and 'ЧЧ' not in s:
            k += 1
print(k)
