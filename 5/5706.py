for n in range(1,1000):
    s=bin(n)[2:]
    if s.count('1')%2==0:
        s1='10'+s[2:]+'0'
    else:
        s1='11'+s[2:]+'1'
    r=int(s1,2)
    if r>40:
        print(n)
        break