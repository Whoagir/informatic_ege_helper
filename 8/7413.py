from itertools import *
a='АБОРСУЭ'
comb=product(a,repeat=5)
c=0
v=0
for i in comb:
    v+=1
    s=''.join(i)
    r=s.count('Р')
    y=s.count('У')
    if (y==0) and (r>=2) and ('РР' not in s) and ('РРР' not in s) and ('РРРР' not in s) and ('РРРРР' not in s) and v%2==0:
        c+=1
print(c)