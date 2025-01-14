def F(n):
    if n<=3:
        return n
    if n>3 and n%2==0:
        return n+F(n-1)
    if n>3 and n%2!=0:
        return n*n+F(n-2)
c=0
for n in range(1,1000):
    if F(n)>100000000:
        break
    c+=1
print(c)