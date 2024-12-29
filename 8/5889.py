from itertools import *

a = 'КОНФЕТА'
a1 = 'ОЕА'
comb = product(a, repeat=5)
combE3 = product(a1, repeat=3)
combE2 = product(a1, repeat=2)
c = 0
ex = []
for j in combE3:
    s1 = ''.join(j)
    ex.append(s1)
for v in combE2:
    s2 = ''.join(v)
    ex.append(s2)

for i in comb:
    s = ''.join(i)
    o = s.count('О')
    e = s.count('Е')
    n = s.count('А')
    # print(s, n, e, o)
    summa = n + e + o
    if summa >= 2:
        valid = True
        for j in ex:
            if j in s:
                valid = False
                break
        if valid:
            c += 1
print(c)
