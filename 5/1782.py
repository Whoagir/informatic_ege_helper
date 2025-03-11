for n in range(1,1000):
    s=bin(n)[2:]
    s1=s+s[-1]
    if s.count('1')%2==0:
        s2=s1+'0'
    else:
        s2=s1+'1'
    if s2.count('1')%2!=0:
        s2=s2+'1'
    r=int(s2,2)
    if r>160:
        print(n)
        break