for n in range(100,1,-1):
    s=bin(n)[2:]
    s1=s[::-1]
    r=int(s1,2)
    if r==7:
        print(n)
        break