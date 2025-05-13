from itertools import *
pr=[2,3,5,7,11,13,17]
a='01234567'
c=0
comb=product(a,repeat=5)
for i in comb:
    s=''.join(i)
    f=0
    for x in range(5):
        for y in range(x+1,5):
            if s[x]!=s[y] and (int(s[x])+int(s[y])) in pr and s[0]!='0':
                f=1
    if f>=1:
        c+=1
print(c)