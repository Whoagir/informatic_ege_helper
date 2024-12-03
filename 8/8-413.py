# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('012345678', repeat = 4):
    s = ''.join(s)
    if s[0] != '0' and s.count('6') <= 2:
        for el in '0248':
            s = s.replace(el, 'Ч')
        if '6Ч' not in s and 'Ч6' not in s and '66' not in s:
            k += 1
print(k)
