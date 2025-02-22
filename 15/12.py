for a in range(100,1,-1):
    c=0
    for x in range(1,1001):
        f=(a<50) and ((not x%a==0)<=((x%10==0)<= (not x%12==0)))
        if f:
            c+=1
    if c==1000:
        print(a)
        break