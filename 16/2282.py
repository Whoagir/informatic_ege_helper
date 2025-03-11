def f(n):
    if n>30:
        return n*n+5*n+4
    if n<=30 and n%2==0:
        return f(n+1)+3*f(n+4)
    if n<=30 and n%2!=0:
        return 2*f(n+2)+f(n+5)
c=0
for n in range(1,1001):
    if sum(map(int,str(f(n))))==27:
        c+=1
print(c)