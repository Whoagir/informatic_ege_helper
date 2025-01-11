for n in range(1,1000):
    v=bin(n)[2:]
    s=v+v[-1]
    m=v.count('1')
    if m%2==0:
        s1=s+'0'
    else:
        s1=s+'1'
    z=s1.count('1')
    if z%2!=0:
        s1=s1+'1'
    r=int(s1,2)
    if r>105:
        print(r)
