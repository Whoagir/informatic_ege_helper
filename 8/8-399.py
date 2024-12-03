# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('0123456789ABC', repeat = 3):
    s = ''.join(s)
    if s[0] != '0' and '8' not in s:
        if len(set(s)) == len(s):
            for el in '02468AC':
                s = s.replace(el, 'Ч')
            for el in '13579B':
                s = s.replace(el, 'Н')
            if 'НН' not in s and 'ЧЧ' not in s:
                k += 1
print(k)
