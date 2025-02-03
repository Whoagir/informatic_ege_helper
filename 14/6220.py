for p in range(100,1,-1):
    for q in range(100,1,-1):
        a=10*p**2+11*p**1+12*p**0
        if (a==11*q**2+12*q**1+13*q**0):
            print(p,q,a)