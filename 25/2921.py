b=[]
a=[]
for n in range(193136,193223):
    e=1000
    c=0
    for m in range(1,int((n**(1/2)))):
        if n%m==0:
            c+=2
            if m<e and m!=1:
                e=m
    if c==6:
        a.append(n)
        b.append(e)
for i in range(len(a)):
    print(a[i],a[i]//b[i])