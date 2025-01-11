from itertools import *
a='ГЕРОЙ'
comb=product(a,repeat=4)
c=0
for i in comb:
    s=''.join(i)
    gl=s.count('Е')+s.count('О')
    if s[0]!='Й' and gl>=1:
        c+=1
print(c)