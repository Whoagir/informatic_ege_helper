from itertools import *
c=0
a='СЕПИЯ'
for x in range(1,8):
    comb=product(a,repeat=x)
    for i in comb:
        s=''.join(i)
        n=s.count('С')
        m=s.count('П')
        if s.count('Е')<=2 and s.count('И')<=2 and s.count('Я')<=2 and m+n<=1:
            if s.count('С')==1 and s.count('П')==0 and s[0]=='С':
                c+=1
            if s.count('П')==1 and s.count('С')--0 and s[0]=='П':
                c+=1
            elif s.count('П')+s.count('С')==0:
                c+=1
print(c)