for a in range(1,800):
    c=0
    for x in range(1,1001):
        f=(x%a==0) <= ((not(x%21==0)) or (x%35==0))
        if f:
            c+=1
    if c==1000:
        print(a)
        break