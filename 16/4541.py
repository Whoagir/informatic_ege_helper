def F(n):
    if n==0:
        return 0
    if n>0 and n%2==0:
        return F(n/2)-1
    if n>0 and n%2!=0:
        return 1+F(n-1)
c=0
for n in range (0,1000):
    if F(n)==0:
        c+=1
print(c)