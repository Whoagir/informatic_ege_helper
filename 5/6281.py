for n in range(1000,1,-1):
    s=bin(n)[2:]
    if n%4==0:
        s1=s+s[-2:]
    else:
        s1=bin(n%4*2)[2:]+s
    r=int(s1,2)
    if r<68:
        print(n)
        break