for n in range(1000,10000):
    s=str(n)
    cet=0
    for i in s:
        if i%2==0:
            cet=i+cet
    cet2=cet**2
    print(s,cet2)
    m=int(max(s[0],s[1],s[2],s[3]))-int(max(s[0],s[1],s[2],s[3]))
    m3=m**3
    print()
    if cet2>=m3:
        s2=str(cet2)+str(m3)
    else:
        s2=str(m3)+str(cet2)