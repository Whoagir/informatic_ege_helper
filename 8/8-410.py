# Автор: М. Ишимов

from itertools import *
k = 0
for s in product('012345678', repeat = 5):
    s = ''.join(s)
    if s[0] != '0' and s.count('5') == 1:
        for el in '137':
            s = s.replace(el, 'Н')
        if '5Н' in s:
            k += 1
print(k)
