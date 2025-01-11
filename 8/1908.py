from itertools import *
a='РАДУГ'
comb=product(a,repeat=6)
c=0
for i in comb:
    s=''.join(i)
    v=s.count('Р')
    v1=s.count('Д')
    v2=s.count('Г')
    sogl=v+v1+v2
    if sogl>=3:
        c+=1
print(c)