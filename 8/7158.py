from itertools import *
a='ГЕНОСТ'
comb=product(a,repeat=4)
c=1
for i in comb:
    s=''.join(i)
    c+=1
    v=s.count('О')
    if c%2!=0 and s[0]!='Н' and v>=2 and 'С' not in s:
        print(c,s)
