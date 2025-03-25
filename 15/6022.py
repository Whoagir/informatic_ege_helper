for a in range(1,800):
    c=0
    for x in range(1,1001):
        for y in range(1,1001):
            f=(x<a) or (y<a) or (x+2*y>150)
            if f:
                c+=1
        if c==1000:
            print(a)
            break