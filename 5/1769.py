for n in range(1000,2000):
    s=bin(n)[2:]
    s1=s[::-1]
    r=int(s1,2)
    if r==29:
        print(r,n)