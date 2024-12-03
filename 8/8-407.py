# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('0123456789AB', repeat = 5):
    s = ''.join(s)
    if s[0] != '0' and s.count('2') == 1:
        for el in '0468A':
            s = s.replace(el, 'Ч')
        for el in '13579B':
            s = s.replace(el, 'Н')
        if '2Ч' in s and 'Н' not in s[s.index('2') + 1:]:
            k += 1
print(k)
