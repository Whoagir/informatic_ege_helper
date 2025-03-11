for a in range(1,800):
    c=0
    for x in range(1,1001):
        f=(a%12==0) and ((530%x==0)<=((not(a%x==0))<=(not 170%x==0)))
        if f:
            c+=1
    if c==1000:
        print(a)
        break