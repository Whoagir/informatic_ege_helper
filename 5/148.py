for n in range(1,1000):
    s=bin(n)[2:]
    s1=s+str(s.count('1')%2)
    s2= s1 + str(s1.count('1') % 2)
    r=int(s2,2)
    if r>130:
        print(r)
        break