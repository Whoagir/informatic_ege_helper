for n in range(1000,1,-1):
    s=bin(n)[2:]
    if s.count('1')%3==0:
        s1=s+s[0:2]
    else:
        m=(s.count('1')%3)*3
        s1=bin(m)[2:]+s
    r=int(s1,2)
    if r<60:
        print(r,n)
        break