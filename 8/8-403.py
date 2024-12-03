# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('012345', repeat = 3):
    s = ''.join(s)
    if s[0] != '0' and s.count('5') == 1:
        for el in '024':
            s = s.replace(el, 'Ч')
        if '5Ч' not in s and 'Ч5' not in s:
            k += 1
print(k)
