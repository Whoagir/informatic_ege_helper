def ctb(n:int,b:int)->str:
    r=''
    while n>0:
        d=str(n%b)
        r=d+r
        n//=b
    return r
s=19**81+23**709-4
s1=ctb(s,9)
