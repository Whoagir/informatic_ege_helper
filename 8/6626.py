from itertools import *
a='ЬРПЛЕА'
comb=product(a,repeat=5)
c=1
ans=0
for i in comb:
    s=''.join(i)
    c+=1
    if s[-1]=='Ь':
        ans+=1
    if c==387:
        print(ans)
        break