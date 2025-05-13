from itertools import *
c=0
a='СЕПИЯ'
for x in range(3,8):
    comb=product(a,repeat=x)
    for i in comb:
        s=''.join(i)
        n=s.count('С')
        m=s.count('П')
        if s.count('Е')>2 or s.count('И')>2 or s.count('Я')>2:
            continue
        if 'С' in s[1:] or 'П' in s[1:]:
            continue
        c+=1
print(c)