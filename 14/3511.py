def ctb(n:int,b:int)->str:
    r=''
    while n>0:
        d=str(n%b)
        r=d+r
        n//=b
    return r
s=5**2004-5**1016-25**508-5*400+25**250-27
print(s)
s1=ctb(s,5)
print(s1)
c=s1.count('4')
print(c)
