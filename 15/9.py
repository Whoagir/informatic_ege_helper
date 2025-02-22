p=[i for i in range(5,31)]
q=[i for i in range(14,24)]
c=0
for amin in range(1,30):
    for amax in range(amin+1,30):
        chek=1
        a=[i for i in range(amin,amax)]
        for x in range(1,35):
            f=((x in p)==(x in q))<=(not(x in a))
            if not f:
                chek=0
                break
        if chek==1:
            c=max(c,amax-amin)
print(c)