# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('012', repeat = 6):
    s = ''.join(s)
    if s[0] != '0' and s.count('2') == 1:
        for el in '0':
            s = s.replace(el, 'Ч')
        if '2Ч' in s:
            k += 1
print(k)
