for n in range(1,1000):
    s=bin(n)[2:]
    if n%2==0:
        s1='1'+s+'0'
    else:
        s1='11'+s+'11'
    r=int(s1,2)
    if r>225:
        print(r)
        break