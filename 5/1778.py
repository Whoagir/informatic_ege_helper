for n in range(1,1000):
    s=bin(n)[2:]
    s1=s+s[-1]
    if s.count('1')%2==0:
        s3=s1+'0'
    else:
        s3=s1+'1'
    if s3.count('1')%2!=0:
        s4=s3+'1'
    else:
        s4='0'+s3
    r=int(s4,2)
    if r>130:
        print(r)
        break