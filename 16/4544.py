def F(n):
    if n==0:
        return 0
    elif n>0 and n%2==0:
        return F(n//2)-1
    else:
        return 3+F(n-1)
c=0
a=set()
for n in range (1,1000):
    a.add(F(n))
print(len(a))