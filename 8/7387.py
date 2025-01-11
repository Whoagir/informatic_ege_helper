from itertools import *
a='АИКМНОПЯ'
number=1
c=0
comb=product(a,repeat=6)
for i in comb:
    s=''.join(i)
    v=s.count('И')
    if v==3 and s[0]!='М' and number%2!=0:
        c+=1
    number+=1
print(c)