for a in range(1,800):
    c=0
    for x in range(1,1001):
        f=(a+x<123) <= ((x%5==0)<=((not(x%7==0))))
        if f:
            c+=1
    if c==1000:
        print(a)
        break