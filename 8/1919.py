from itertools import *
a='ВОРОТА'
comb=permutations(a, r=6)
c=0
ans=set()
for i in comb:
    s=''.join(i)
    if 'ОО' not in s and 'АА' not in s and 'АО' not in s and 'ОА' not in s:
        ans.add(s)
print(len(ans))