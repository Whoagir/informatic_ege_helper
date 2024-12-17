from functions import ctb
c=0
for x in range(1,1000000):
    s=7**400+7**300-x
    r=ctb(s,7)
    b=r.count('0')
    if b>c:
        c=b
print(c)