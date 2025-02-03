for n in range(1,1000):
    s=bin(n)[2:]
    v=s.rfind('0')
    s1=s[:v]+s[:2]+s[v+1:]
    # print(s,v,s1)
    s2=s1[::-1]
    r=int(s2,2)
    if r==119:
        print(r,n)