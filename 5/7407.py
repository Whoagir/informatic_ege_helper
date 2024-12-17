def ctb(n: int, b: int) -> str:
    r=''
    while n>0:
        d=str(n%b)
        r=d+r
        n//=b
    return r
for n in range(1,1000):
    s=ctb(n,3)
    b=s[-1]
    b1=s[0]
    if n%2==0:
        s1='2'+s+ctb(int(b)*2,3)
    else:
        s1=ctb(int(b1)*2,3)+s+'2'
    r=int(s1,3)
    if r>100:
        print(r)