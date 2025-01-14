from itertools import *
a='0123456789AB'
c=0
comb=product(a,repeat=7)
for i in comb:
    s=''.join(i)
    b1=int(s[0],12)
    b2 = int(s[1], 12)
    b3 = int(s[2], 12)
    b4 = int(s[3], 12)
    b5 = int(s[4], 12)
    b6 = int(s[5], 12)
    b7 = int(s[6], 12)
    if b1!=0 and b1%3==0 and b2%3!=0 and b3%3==0 and b4%3!=0 and b5%3==0 and b6%3!=0 and b7%3==0:
        c+=1
    elif b1!=0 and b1%3!=0 and b2%3==0 and b3%3!=0 and b4%3==0 and b5%3!=0 and b6%3==0 and b7%3!=0:
        c+=1
print(c)