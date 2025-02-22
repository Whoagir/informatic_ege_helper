from itertools import *
a='СВЯТОЛА'
c=0
comb=product(a,repeat=7)
for i in comb:
    s=''.join(i)
    gl=s.count('А')+s.count('Я')+s.count('О')
    sogl=s.count('С')+s.count('В')+s.count('Т')++s.count('Л')
    if gl>sogl:
        c+=1
print(c)