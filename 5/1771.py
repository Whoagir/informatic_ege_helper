for n in range (1,1000):
    s=bin(n)[2:]
    s1=s+s[-1]
    if s1.count('1')%2==0:
        s2=s1+'0'
    else:
        s2=s1+'1'
    if s2.count('1')%2==0:
        s3=s2+'0'
    else:
        s3=s2+'1'
    r=int(s3,2)
    if r>144:
        print(r)
        break