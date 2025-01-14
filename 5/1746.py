for n in range(1000,1,-1):
    s=bin(n)[2:]
    null=s.count('0')
    one=s.count('1')
    if one>null:
        s1=s+'1'
    else:
        s1=s+'0'
    r=int(s1,2)
    if r<43:
        print(r)
        break