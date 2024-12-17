for n in range(1,1000):
    s=bin(n)[2:]
    one=s.count('1')
    null=s.count('0')
    if one>null:
        s1=s+'1'
    else:
        s1=s+'0'
    r=int(s1,2)
    if r>36:
        print(r,n)