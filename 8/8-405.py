# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('012345678', repeat = 4):
    s = ''.join(s)
    if s[0] != '0' and s.count('1') == 2:
        for el in '02468':
            s = s.replace(el, 'Ч')
        if '1Ч' not in s and 'Ч1' not in s:
            k += 1
print(k)
