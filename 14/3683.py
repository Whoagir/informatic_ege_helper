def ctb(n:int, b:int)->str:
    r=''
    while n>0:
        d=str(n%b)
        r=d+r
        n//=b
    return r
v=123
for x in range (2,11):
    s=ctb(v,x)
    print (s,x)