for n in range(1,1000):
    s=bin(n)[2:]
    if s.count('1')%2==0:
        s1=s+'1'
    else:
        s1=s+'0'
    if int(s1)%2==0:
        s2=s1+'10'
    else:
        s2=s1+'01'
    r=int(s2,2)
    print(r)