for n in range(4,1000):
    s=bin(n)[2:]
    if n%5==0:
        s1=s+s[-3:]
    else:
        v=(n%5)*5
        v1=bin(v)[2:]
        s1=s+v1
    r=int(s1,2)
    if r<100:
        print(n)