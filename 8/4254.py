from itertools import *
a='01234'
comb=product(a,repeat=5)
c=0
for i in comb:
    s=''.join(i)
    bn=s.count('0')+s.count('2')+s.count('4')
    if s[0]!='0' and bn<=3:
        c+=1
print(c)