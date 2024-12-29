for n in range(96,1000):
    s=bin(n)[2:]
    null=s.count('0')
    one=s.count('1')
    if null==one:
        s1=s+s[-1]
    elif null>one:
        s1=s+'1'
    else:
        s1=s+'0'
    null = s1.count('0')
    one = s1.count('1')
    if null == one:
        s2 = s1 + s1[-1]
    elif null > one:
        s2 = s1 + '1'
    else:
        s2 = s1 + '0'
    null = s2.count('0')
    one = s2.count('1')
    if null == one:
        s3 = s2 + s2[-1]
    elif null > one:
        s3 = s2 + '1'
    else:
        s3 = s2 + '0'
    r=int(s3,2)
    if r%4==0:
        print(n,r)