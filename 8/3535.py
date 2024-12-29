from itertools import *
c=0
a='ДЖОБС'
comb=product(a,repeat=6)
for i in comb:
    s=''.join(i)
    d=s.count('Д')
    o=s.count('О')
    v=s.count('С')
    j=s.count('Ж')
    if d==1 and o==1 and v==1 and j<=2:
        c+=1
print(c)