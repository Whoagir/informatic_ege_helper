for n in range(1000,1,-1):
    s=bin(n)[2:]
    if s.count('1')%2==0:
        s1='11'+s[2:]+'00'
    else:
        s1='10'+s[2:]+'11'
    if s1.count('1')%2==0:
        s2='11'+s1[2:]+'00'
    else:
        s2='10'+s1[2:]+'11'
    r=int(s2,2)
    if r<1500:
        print(r)
        break