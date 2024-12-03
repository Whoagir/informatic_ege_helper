# Автор: И. Карпачев

from itertools import *

ans = 0
for x in product('01234567', repeat=6):
    s = ''.join(x)
    if s[0] != '0' and s.count('4') == 2 and '44' not in s:
        f = s.find('4')
        r = s.rfind('4')
        t = s[f + 1:r]
        ch = s.replace('4', '')
        if all(y in '567' for y in t) and len(ch) == len(set(ch)):
            ans += 1
print(ans)
