from itertools import *
a='КАПКАН'
ans=[]
comb=permutations(a,r=6)
for i in comb:
    s=''.join(i)
    if 'КК' not in s and 'АА' not in s:
        ans.append(s)
d=set(ans)
print(len(d))