for n in range(90,2,-1):
    s=bin(n)[2:]
    one=s.count('1')
    null=s.count('0')
    if one==null:
        s=s+s[-1]
    elif one>null:
        s=s+'0'
    else:
        s=s+'1'
    one=s.count('1')
    null=s.count('0')
    if one==null:
        s=s+s[-1]
    elif one>null:
        s=s+'0'
    else:
        s=s+'1'
    one=s.count('1')
    null=s.count('0')
    if one==null:
        s=s+s[-1]
    elif one>null:
        s=s+'0'
    else:
        s=s+'1'
    r=int(s,2)
    if r%4==0:
        print(r,n)
        break