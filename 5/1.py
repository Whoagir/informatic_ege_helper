for n in range(1,1000):
    s=bin(n)[2:]
    if n%2==0:
        s1='10'+s
    else:
        s1='1'+s+'00'
    r=int(s1,2)
    if n<=12:
        print(r,n)