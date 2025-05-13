from itertools import *
a='АБВГЭЮЯ'
a1='ЭЮЯ'
comb=product(a,repeat=5)
c=0
for i in comb:
    s=''.join(i)
    if (s[0] in a1) and (s[-1] in a1) and not(s[1] in a1):
        c+=1
print(c)