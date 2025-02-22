from itertools import *
a='СПОРТЛОТО'
c=0
d=set()
comb=permutations(a)
for i in comb:
    s=''.join(i)
    v=s.count('О')
    if s[0]=='О' and s[-1]=='О':
        d.add(s)
print(len(d))