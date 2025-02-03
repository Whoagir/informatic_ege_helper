from itertools import *
a='ИНФА'
comb=product(a,repeat=6)
c=0
for i in comb:
    s=''.join(i)
    v=s.count('Ф')
    if v==2:
        c+=1
print(c)