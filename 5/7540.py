for n in range(1,1000):
    s=bin(n)[2:]
    v=s.count('1')
    s1=s+str(v%2)
    v1=s1.count('1')
    s2=s1+str(v1%2)
    r=int(s2,2)
    if r>123:
        print(r)