for n in range(2,10000):
    s=bin(n)[2:]
    s1=s+s[-2]
    s2=s1+s[1]
    r=int(s2,2)
    if r>170:
        print(n)