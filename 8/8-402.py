# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('0123456789ABC', repeat = 3):
    s = ''.join(s)
    if s[0] != '0' and s.count('3') == 2:
        for el in '02468AC':
            s = s.replace(el, 'Ч')
        if 'ЧЧ' not in s:
            k += 1
print(k)
