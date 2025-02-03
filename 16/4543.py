def f(n):
    if n==0:
        return 0
    if n>0 and n%2==0:
        return f(n/2)-1
    if n>0 and n%2!=0:
        return 2+f(n-1)
c=0
for n in range(999,0,-1):
    if f(n)==3:
        c+=1
print(c)