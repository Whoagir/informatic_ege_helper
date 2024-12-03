# Автор: И. Карпачев

from itertools import *

ans = 0
for x in product('01234567', repeat=6):
    s = ''.join(x)
    if s[0] != '0' and s.count('3') == 2 and '33' not in s:
        f = s.find('3')
        r = s.rfind('3')
        t = s[f+1:r]
        if all(y in '4567' for y in t):
            ans += 1
print(ans)
