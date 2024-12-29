def ctb(n:int,b:int)->str:
    r=''
    while n>0:
        d=str(n%b)
        r=d+r
        n//=b
    return r
s=1755
for x in range(2,11):
    s1=ctb(s,x)
    print(s1, x)
