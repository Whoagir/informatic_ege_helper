def F(n):
    if n>25:
        return (n*n)+(4*n)+3
    if n<=25 and n%3==0:
        return F(n+1)+(2*F(n+4))
    if n<=25 and n%3!=0:
        return F(n+2)+(3*F(n+5))
c=0
for n in range (1,1000):
    t = F(n)
    s = sum(int(i) for i in str(t))
    if s==24:
        c+=1
print(c)